 
IF EXIST .\myenv\Scripts\activate.bat (
    CALL .\myenv\Scripts\activate.bat
    python main.py
) ELSE (
    .\myenv\Scripts\activate.bat
    python main.py
)

REM This code will prevent the command prompt window from closing after the program has finished running
pause
