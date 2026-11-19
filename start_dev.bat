@echo off
chcp 936 >nul 2>&1
setlocal
cd /d "%~dp0"

echo ================================
echo SiFli-Wiki 开发服务器启动
echo ================================
echo.

set "VENV_PY=%~dp0venv\Scripts\python.exe"
set "SRC=source\zh_CN"
set "OUT=build"
set "HOST=127.0.0.1"
set "PORT=8000"

REM 检查虚拟环境是否存在
if not exist "%VENV_PY%" (
    echo 错误: 未找到虚拟环境，请先运行 setup_env.bat
    pause
    exit /b 1
)

REM 检查虚拟环境是否可用（虚拟环境目录被移动过时 .exe 启动器会失效，这里改用 python -m 调用）
"%VENV_PY%" -c "import sphinx, sphinx_autobuild" >nul 2>&1
if errorlevel 1 (
    echo 错误: 虚拟环境不可用或缺少依赖。
    echo 请删除 venv 目录后重新运行 setup_env.bat
    pause
    exit /b 1
)

if not exist "%SRC%\conf.py" (
    echo 错误: 未找到 %SRC%\conf.py
    echo 请确认本脚本位于 SiFli-Wiki 项目根目录下
    pause
    exit /b 1
)

echo 正在启动开发服务器...
echo.
echo 服务器信息：
echo - 中文文档: http://%HOST%:%PORT%
echo.
echo 首次构建需要一些时间，构建完成后浏览器会自动打开
echo 按 Ctrl+C 停止服务器
echo.

"%VENV_PY%" -m sphinx_autobuild "%SRC%" "%OUT%" --host %HOST% --port %PORT% --open-browser

echo.
echo 服务器已停止
pause
