@echo off
cls

call rmdir /s /q .git

call .\.venv\Scripts\activate
call .\.venv\Scripts\python clean.py

call git init

call git remote add origin https://github.com/sergeyyurkov1/pythonui.git

call git add *

call git commit --all --message="commit"

call git push --force origin main

pause
