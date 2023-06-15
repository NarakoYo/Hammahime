:: start.bat
:: 这是一个bat文件，用于一键启动node.js可移植版和server.js脚本
@echo off
:: 切换到html目录
cd /d %~dp0
:: 启动node.js可移植版和server.js脚本
start .\node.exe server.js
:: 打开浏览器访问http://localhost:3000
start iexplore http://localhost:3000
:: 退出bat文件
exit
