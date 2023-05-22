 
@echo off

call .\py311\Scripts\activate.bat&&.\py311\python.exe .\main.py

REM This code will prevent the command prompt window from closing after the program has finished py311
pause
