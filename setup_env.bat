@echo off
chcp 65001 >nul 2>&1
echo ================================
echo SiFli-Wiki 开发环境设置脚本
echo ================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 请先安装 Python 3.7+ 版本
    echo 下载地址: https://mirrors.ustc.edu.cn/python/3.12.0/python-3.12.0.exe
    pause
    exit /b 1
)

echo 检测到 Python 版本:
python --version

echo.
echo 正在创建虚拟环境...
python -m venv venv
if %errorlevel% neq 0 (
    echo 错误: 虚拟环境创建失败
    pause
    exit /b 1
)

echo 正在激活虚拟环境...
call venv\Scripts\activate.bat

echo 正在升级 pip...
python -m pip install --upgrade pip -i https://mirrors.ustc.edu.cn/pypi/simple --trusted-host mirrors.ustc.edu.cn

echo 正在安装依赖包...
pip install -r requirements.txt -i https://mirrors.ustc.edu.cn/pypi/simple --trusted-host mirrors.ustc.edu.cn
if %errorlevel% neq 0 (
    echo 错误: 依赖包安装失败
    pause
    exit /b 1
)

echo.
echo ================================
echo 环境设置完成！
echo ================================
echo.
echo 使用说明：
echo 1. 运行 start_dev.bat 启动开发服务器
echo 2. 运行 build_docs.bat 构建文档
echo 3. 运行 clean.bat 清理构建文件
echo.
pause
