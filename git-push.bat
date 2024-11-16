@echo off
cls

call git add --chmod=+x ./goodies/mhy
call git add --chmod=+x ./goodies/weather
call git add --chmod=+x ./goodies/sw
call git add --chmod=+x ./goodies/test/01
call git add --chmod=+x ./goodies/test/02

call git add *

call git commit --all --message="commit"

call git push origin main

pause
