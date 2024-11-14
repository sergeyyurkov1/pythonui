@echo off
cls

call git add *

call git commit --all --message="commit"

call git push origin main

pause
