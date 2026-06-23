"""SEO helpers for SiFli Wiki."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx


NOINDEX_PAGES = {"genindex", "search"}


SPECIFIC_DESCRIPTIONS = {
    ("zh_CN", "index"): (
        "思澈 SiFli Wiki 提供低功耗蓝牙 MCU、LVGL 图形界面、智能手表和 AIoT 产品开发资料，"
        "涵盖芯片选型、开发板、硬件设计、SDK、工具和常见问题。"
    ),
    ("en", "index"): (
        "SiFli Wiki provides low-power Bluetooth MCU, LVGL graphics, smartwatch and AIoT product "
        "development resources, including chips, boards, hardware design, SDK tools and FAQs."
    ),
    ("zh_CN", "silicon/product-index"): (
        "SiFli 产品索引汇总低功耗蓝牙 MCU、开发板、规格书和硬件资料，覆盖 LVGL 图形、"
        "智能手表、穿戴设备和 AIoT 产品选型。"
    ),
    ("en", "silicon/product-index"): (
        "SiFli product index for low-power Bluetooth MCUs, development boards, datasheets and hardware "
        "resources for LVGL graphics, smartwatches, wearables and AIoT product selection."
    ),
    ("zh_CN", "board/sf32lb52x/SF32LB52-DevKit-Core-3p3"): (
        "SF32LB52-DevKit-Core-3p3 开发板使用指南，介绍板卡概览、引脚、供电、GPIO、UART、I2C、"
        "SPI、LCD、I2S、音频和资料下载，适合低功耗蓝牙、LVGL 和智能手表原型验证。"
    ),
    ("en", "board/sf32lb52x/SF32LB52-DevKit-Core-3p3"): (
        "SF32LB52-DevKit-Core-3p3 development board guide covering overview, pinout, power, GPIO, UART, "
        "I2C, SPI, LCD, I2S, audio and downloads for low-power Bluetooth, LVGL and smartwatch prototypes."
    ),
    ("zh_CN", "board/sf32lb52x/SF-DevKit-LCM-Adapter"): (
        "SiFli 开发板 LCM 转接板制作指南，说明 SPI、QSPI、RGB、DSI 和 MCU-8080 显示接口定义，"
        "支持 LVGL、智能手表屏幕和低功耗蓝牙产品调试。"
    ),
    ("en", "board/sf32lb52x/SF-DevKit-LCM-Adapter"): (
        "SiFli DevKit LCM adapter guide for SPI, QSPI, RGB, DSI and MCU-8080 display interfaces, supporting "
        "LVGL, smartwatch displays and low-power Bluetooth product debugging."
    ),
}


ZH_CATEGORY_DESCRIPTIONS = [
    (
        "board/",
        "{title}，介绍 SiFli 开发板功能、引脚、供电、外设接口、原理图和资料下载，适合低功耗蓝牙、LVGL 显示和智能手表产品验证。",
    ),
    (
        "hardware/",
        "{title}，提供 SiFli 芯片硬件设计指南、供电、时钟、Flash、LCD、音频和接口设计建议，面向低功耗蓝牙、LVGL 和智能手表 AIoT 产品。",
    ),
    (
        "silicon/",
        "{title}，汇总 SiFli 低功耗蓝牙 MCU 型号、规格书、开发板和硬件资料，覆盖 LVGL 图形、智能手表和 AIoT 应用选型。",
    ),
    (
        "tools/",
        "{title}，介绍 SiFli 开发工具、烧录、屏幕调试、图形转换和 Flash 配置，支持低功耗蓝牙、LVGL 和智能手表产品开发。",
    ),
    (
        "faq/",
        "{title}，整理 SiFli SDK、硬件、外设、调试和开发工具常见问题，服务低功耗蓝牙、LVGL、智能手表和 AIoT 产品开发。",
    ),
    (
        "appnote/",
        "{title}，提供 SiFli 应用笔记和开发实践，覆盖低功耗、蓝牙、LVGL、智能手表、硬件调试和 AIoT 产品落地。",
    ),
    (
        "application/",
        "{title}，展示 SiFli 低功耗蓝牙 MCU 在 LVGL 图形、智能手表、穿戴设备和 AIoT 产品中的应用方案。",
    ),
    (
        "module/",
        "{title}，介绍 SiFli 模组资料和选型信息，面向低功耗蓝牙、LVGL、智能手表和 AIoT 产品快速开发。",
    ),
    (
        "docs/",
        "{title}，提供 SiFli SDK 和开发入门资料，帮助开发者构建低功耗蓝牙、LVGL、智能手表和 AIoT 产品。",
    ),
    (
        "about/",
        "{title}，介绍思澈科技低功耗蓝牙 MCU、LVGL 图形、智能手表和 AIoT 产品方向、公司能力和联系方式。",
    ),
]


EN_CATEGORY_DESCRIPTIONS = [
    (
        "board/",
        "{title}. SiFli development board guide with features, pinout, power, interfaces, schematics and downloads for low-power Bluetooth, LVGL display and smartwatch products.",
    ),
    (
        "hardware/",
        "{title}. SiFli hardware design resources for power, clock, Flash, LCD, audio and interfaces in low-power Bluetooth, LVGL and smartwatch AIoT products.",
    ),
    (
        "silicon/",
        "{title}. SiFli low-power Bluetooth MCU models, datasheets, development boards and hardware resources for LVGL graphics, smartwatches and AIoT selection.",
    ),
    (
        "tools/",
        "{title}. SiFli development tools for flashing, display debugging, graphics conversion and Flash configuration for low-power Bluetooth, LVGL and smartwatch products.",
    ),
    (
        "faq/",
        "{title}. SiFli SDK, hardware, peripheral, debugging and tool FAQs for low-power Bluetooth, LVGL, smartwatch and AIoT product development.",
    ),
    (
        "appnote/",
        "{title}. SiFli application notes and development practices covering low power, Bluetooth, LVGL, smartwatches, hardware debugging and AIoT products.",
    ),
    (
        "application/",
        "{title}. SiFli low-power Bluetooth MCU application resources for LVGL graphics, smartwatches, wearables and AIoT products.",
    ),
    (
        "module/",
        "{title}. SiFli module resources and selection information for low-power Bluetooth, LVGL, smartwatch and AIoT product development.",
    ),
    (
        "docs/",
        "{title}. SiFli SDK and getting-started resources for building low-power Bluetooth, LVGL, smartwatch and AIoT products.",
    ),
    (
        "about/",
        "{title}. About SiFli Technologies, low-power Bluetooth MCUs, LVGL graphics, smartwatch and AIoT product capabilities.",
    ),
]


def _strip_markup(value: Any) -> str:
    text = re.sub(r"<[^>]+>", "", str(value or ""))
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _truncate(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip(" ,，。.;；") + "。"


def _source_text(app: Sphinx, pagename: str) -> str:
    try:
        source = Path(app.env.doc2path(pagename, base=None))
    except Exception:
        return ""
    if not source.is_file():
        return ""
    try:
        return source.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def _detect_keywords(text: str, language: str) -> str:
    lower = text.lower()
    if language == "zh_CN":
        found = []
        for needle, label in [
            ("低功耗", "低功耗"),
            ("bluetooth", "蓝牙"),
            ("蓝牙", "蓝牙"),
            ("lvgl", "LVGL"),
            ("手表", "智能手表"),
            ("watch", "智能手表"),
            ("lcd", "LCD 显示"),
            ("display", "显示"),
            ("flash", "Flash"),
        ]:
            if needle.lower() in lower and label not in found:
                found.append(label)
        if found:
            return "重点覆盖" + "、".join(found[:5]) + "。"
        return ""

    found = []
    for needle, label in [
        ("low power", "low power"),
        ("low-power", "low power"),
        ("bluetooth", "Bluetooth"),
        ("lvgl", "LVGL"),
        ("watch", "smartwatch"),
        ("lcd", "LCD display"),
        ("display", "display"),
        ("flash", "Flash"),
    ]:
        if needle in lower and label not in found:
            found.append(label)
    if found:
        return "Covers " + ", ".join(found[:5]) + "."
    return ""


def _category_description(language: str, pagename: str, title: str) -> str:
    descriptions = ZH_CATEGORY_DESCRIPTIONS if language == "zh_CN" else EN_CATEGORY_DESCRIPTIONS
    for prefix, template in descriptions:
        if pagename.startswith(prefix):
            return template.format(title=title)
    if language == "zh_CN":
        return (
            f"{title}，SiFli Wiki 提供低功耗蓝牙 MCU、LVGL 图形界面、智能手表和 AIoT 产品开发资料，"
            "涵盖芯片、开发板、硬件设计、SDK、工具和常见问题。"
        )
    return (
        f"{title}. SiFli Wiki provides low-power Bluetooth MCU, LVGL graphics, smartwatch and AIoT "
        "product development resources, including chips, boards, hardware, SDK tools and FAQs."
    )


def make_description(app: Sphinx, pagename: str, title: str) -> str:
    language = app.config.language or "en"
    if (language, pagename) in SPECIFIC_DESCRIPTIONS:
        return SPECIFIC_DESCRIPTIONS[(language, pagename)]

    text = _source_text(app, pagename)
    description = _category_description(language, pagename, title)
    keywords = _detect_keywords(text, language)
    if keywords and keywords not in description:
        description = f"{description} {keywords}"
    return _truncate(description, 180 if language == "zh_CN" else 165)


def update_page_context(app: Sphinx, pagename: str, templatename: str, context: dict[str, Any], doctree: Any) -> None:
    context["seo_noindex"] = pagename in NOINDEX_PAGES

    if pagename in NOINDEX_PAGES:
        return

    title = _strip_markup(context.get("title")) or app.config.project
    description = make_description(app, pagename, title)

    meta = context.get("meta")
    if not isinstance(meta, dict):
        meta = {}
        context["meta"] = meta

    if not meta.get("description"):
        meta["description"] = description

    context["seo_description"] = meta["description"]


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("html-page-context", update_page_context)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": "1.0",
    }
