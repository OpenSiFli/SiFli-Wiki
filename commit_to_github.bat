@echo off
chcp 65001 > nul
echo ================================
echo 提交更改到 GitHub
echo ================================
echo.

REM 激活虚拟环境
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo 警告: 虚拟环境未找到，请先运行 setup_env.bat
    echo.
)

REM 检查 Git 状态
echo 1. 检查当前 Git 状态...
git status
echo.

REM 询问是否继续
set /p continue="是否继续提交？(y/N): "
if /i not "%continue%"=="y" (
    echo 操作已取消
    pause
    exit /b 0
)

echo.
echo 2. 添加文件到暂存区...

REM 添加源文件
git add source/
echo    ✓ 已添加 source/ 目录

REM 添加构建脚本
git add *.bat *.sh *.ps1 2>nul
echo    ✓ 已添加脚本文件

REM 添加配置文件
git add requirements.txt README*.md 2>nul
echo    ✓ 已添加配置和文档文件

REM 检查是否有文件被添加
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo.
    echo 没有文件需要提交
    pause
    exit /b 0
)

echo.
echo 3. 查看将要提交的更改...
git diff --cached --stat
echo.

REM 获取提交消息
set /p commit_message="请输入提交消息: "
if "%commit_message%"=="" (
    set commit_message=更新文档
)

echo.
echo 4. 提交更改...
git commit -m "%commit_message%"

if %errorlevel% neq 0 (
    echo 提交失败！
    pause
    exit /b 1
)

echo    ✓ 提交成功

echo.
echo 5. 推送到 GitHub...
git push origin main

if %errorlevel% neq 0 (
    echo 推送失败！请检查网络连接或权限设置
    echo.
    echo 可能的解决方案：
    echo - 检查网络连接
    echo - 确认 GitHub 访问权限
    echo - 手动运行: git push origin main
    pause
    exit /b 1
)

echo    ✓ 推送成功！

echo.
echo ================================
echo 所有更改已成功提交到 GitHub！
echo ================================
echo.
echo 您可以在以下地址查看更改：
echo https://github.com/OpenSiFli/SiFli-Wiki
echo.
pause
