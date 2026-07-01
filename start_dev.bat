@echo off
chcp 65001 >nul 2>&1
echo ================================
echo SiFli-Wiki 开发服务器启动
echo ================================

REM 检查虚拟环境是否存在
if not exist "venv\Scripts\sphinx-autobuild.exe" (
    echo 错误: 虚拟环境不存在或未安装依赖，请先运行 setup_env.bat
    pause
    exit /b 1
)

echo 正在启动开发服务器...
echo.
echo 服务器信息：
echo - 中文文档: http://localhost:8000
echo - 英文文档: http://localhost:8000/en
echo.
echo 按 Ctrl+C 停止服务器
echo.

REM 延迟后打开浏览器
start "" cmd /c "timeout /t 8 /nobreak >nul && start http://127.0.0.1:8000"

REM 启动sphinx-autobuild进行实时预览
venv\Scripts\sphinx-autobuild.exe source\zh_CN build --host 127.0.0.1 --port 8000 --open-browser

