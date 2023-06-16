:: start.bat
chcp 65001
:: 这是一个bat文件，用于一键启动node.js可移植版和server.js脚本
@echo off
:: 切换到html所在目录
cd /d %~dp0

echo 从ApplicationConfig.yaml文件中读取端口号
for /f "tokens=2 delims=:" %%a in ('findstr /c:"port:" ApplicationConfig.yaml') do set port=%%a
rem 去掉端口号前后的空格
set port=%port: =%
echo "读取端口号为"+"%port%"
echo 查找占用端口的进程ID
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c:":%port%"') do set pid=%%a
echo 判断是否存在占用端口的进程
if defined pid (
  echo %pid%占用%port%端口，无法启动
)
echo 不存在占用端口%port%
@REM pause

echo 启动node.js可移植版和server.js脚本
@REM start .\node.exe server.js
@REM echo 启动node.js可移植版和server.js脚本并隐藏命令行
start .\start.vbs

:: 打开浏览器访问http://localhost:3000
echo start iexplore http://localhost:%port%

for /l %%i in (3,-1,1) do ( echo %%i & ping -n 2 127.0.0.1 >nul)
start iexplore http://localhost:%port%
@REM choice /t 3 /d y /n >nul
:: 退出bat文件
@REM pause
exit