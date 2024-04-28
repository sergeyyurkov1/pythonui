@echo off
cls

call rmdir /s /q .git

call .\.venv\Scripts\activate
call .\.venv\Scripts\python clean.py

echo init
call git init
echo git remote add origin
call git remote add origin https://github.com/sergeyyurkov1/pythonui.git
echo git add
call git add *

echo git commit
call git commit --all --message="commit"

@REM call git tag -a v1.0 -m "Release version 1.0"

echo git push
call git push --force origin main
@REM v1.0
@REM --tags

pause
