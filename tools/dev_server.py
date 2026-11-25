#!/usr/bin/env python
"""SiFli-Wiki 本地双语开发服务器。

start_dev.bat / start_dev_gbk.bat 原来只构建 source/zh_CN 到 build/，
英文站（source/en -> build/en）从未构建，所以点击语言切换后
http://127.0.0.1:8000/en/ 会直接 Not Found。

本脚本的行为：
1. 先把英文站构建到 build/en（与 CI 的 scripts/build_parallel_docs.sh 一致）；
2. 再启动 sphinx-autobuild 服务中文站（默认 http://127.0.0.1:8000/）；
3. 后台轮询 source/en、source/_static、source/_templates 的修改时间，
   有变化就增量重建 build/en，英文页刷新即可看到最新内容。

用法：
    python tools/dev_server.py [--host 127.0.0.1] [--port 8000]
                               [--open-browser] [--no-en]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH_SRC = ROOT / "source" / "zh_CN"
EN_SRC = ROOT / "source" / "en"
OUT = ROOT / "build"
DOCTREE = ROOT / ".sphinx-doctrees"
POLL_SECONDS = 2.0

WATCH_DIRS = [EN_SRC, ROOT / "source" / "_static", ROOT / "source" / "_templates"]


def log(msg: str) -> None:
    print(msg, flush=True)


def build_english() -> bool:
    """增量构建英文站到 build/en。返回是否成功。"""
    cmd = [
        sys.executable,
        "-m",
        "sphinx",
        "-b",
        "html",
        "-d",
        str(DOCTREE / "en"),
        str(EN_SRC),
        str(OUT / "en"),
        "-q",
    ]
    started = time.time()
    result = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    cost = time.time() - started
    if result.returncode != 0:
        log("[英文站] 构建失败：")
        log((result.stderr or result.stdout or "").strip()[-2000:])
        return False
    log(f"[英文站] 构建完成（{cost:.1f}s）-> {OUT / 'en'}")
    return True


def snapshot() -> float:
    """返回被监视目录中最新的文件修改时间。"""
    latest = 0.0
    for base in WATCH_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file():
                try:
                    mtime = path.stat().st_mtime
                except OSError:
                    continue
                if mtime > latest:
                    latest = mtime
    return latest


def watch_english(stop: threading.Event) -> None:
    last = snapshot()
    while not stop.wait(POLL_SECONDS):
        current = snapshot()
        if current > last:
            last = current
            log("[英文站] 检测到修改，正在重建…")
            build_english()
            # 构建过程本身不会写入受监视目录，这里再取一次快照避免重复触发
            last = max(last, snapshot())


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="SiFli-Wiki 双语开发服务器")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--open-browser", action="store_true")
    parser.add_argument("--no-en", action="store_true", help="跳过英文站构建与监听")
    args = parser.parse_args()

    if not (ZH_SRC / "conf.py").is_file():
        log(f"错误：未找到 {ZH_SRC / 'conf.py'}")
        return 1
    if not args.no_en and not (EN_SRC / "conf.py").is_file():
        log(f"错误：未找到 {EN_SRC / 'conf.py'}")
        return 1

    stop = threading.Event()
    watcher: threading.Thread | None = None

    if not args.no_en:
        log("正在构建英文站（首次约 20-30 秒）…")
        build_english()
        watcher = threading.Thread(target=watch_english, args=(stop,), daemon=True)
        watcher.start()

    base = f"http://{args.host}:{args.port}"
    log("")
    log("服务器信息：")
    log(f"- 中文文档: {base}/")
    if not args.no_en:
        log(f"- 英文文档: {base}/en/")
    log("- 修改中文源文件会自动重建并刷新浏览器；修改英文源文件约 2 秒后自动重建，手动刷新即可")
    log("按 Ctrl+C 停止服务器")
    log("")

    cmd = [
        sys.executable,
        "-m",
        "sphinx_autobuild",
        str(ZH_SRC),
        str(OUT),
        "--host",
        args.host,
        "--port",
        str(args.port),
    ]
    if args.open_browser:
        cmd.append("--open-browser")

    try:
        return subprocess.call(cmd, cwd=str(ROOT))
    except KeyboardInterrupt:
        return 0
    finally:
        stop.set()
        if watcher is not None:
            watcher.join(timeout=POLL_SECONDS + 1)


if __name__ == "__main__":
    raise SystemExit(main())
