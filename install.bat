@echo off
cls
call .\.venv\Scripts\activate
call .\.venv\Scripts\python -m pip install --upgrade -r requirements.txt
pause
