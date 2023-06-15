:: start.bat
chcp 65001
:: 这是一个bat文件，用于一键启动node.js可移植版和server.js脚本
@echo off
:: 切换到html所在目录
cd /d %~dp0

echo 从ApplicationConfig.yaml文件中读取端口号
for /f "tokens=2 delims=:" %%a in ('findstr /c:"post:" ApplicationConfig.yaml') do set port=%%a
rem 去掉端口号前后的空格
set port=%port: =%
echo "读取端口号为"+"%port%"
echo 查找占用端口的进程ID
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /c:":%port%"') do set pid=%%a
echo 判断是否存在占用端口的进程
if defined pid (
  echo 终止占用端口的进程
  taskkill /f /pid %pid%
)
echo 不存在占用端口 
@REM pause

:: 启动node.js可移植版和server.js脚本
@REM start .\node.exe server.js
echo 启动node.js可移植版和server.js脚本并隐藏命令行
start .\start.vbs

:: 打开浏览器访问http://localhost:3000
start iexplore http://localhost:3000

for /l %%i in (3,-1,1) do ( echo %%i & ping -n 2 127.0.0.1 >nul)
@REM choice /t 3 /d y /n >nul
:: 退出bat文件
@REM pause
exit