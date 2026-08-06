@echo off
chcp 65001 >nul 2>&1
echo ================================
echo SiFli-Wiki 开发服务器启动
echo ================================

REM 检查虚拟环境是否存在
if not exist "venv\Scripts\activate.bat" (
    echo 错误: 虚拟环境不存在，请先运行 setup_env.bat
    pause
    exit /b 1
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

echo 正在启动开发服务器...
echo.
echo 服务器信息：
echo - 中文文档: http://localhost:8000
echo - 英文文档: http://localhost:8000/en
echo.
echo 按 Ctrl+C 停止服务器
echo.

REM 启动sphinx-autobuild进行实时预览
sphinx-autobuild source build --host 127.0.0.1 --port 8000 --open-browser
