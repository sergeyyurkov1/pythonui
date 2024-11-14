@echo off
cls
call .\.venv\Scripts\activate
start cmd.exe /c ".\.venv\Scripts\textual console"
timeout /t 5
call .\.venv\Scripts\textual run --dev app.py
pause
