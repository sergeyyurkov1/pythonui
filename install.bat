@echo off
cls
call .\.venv\Scripts\activate
call .\.venv\Scripts\python -m pip install -r requirements.txt
pause
