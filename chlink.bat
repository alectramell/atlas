@echo off

cls

set ip=www.google.com

cls

ping -n 1 %ip% | find "TTL"

cls

if not errorlevel 1 set error=1
if errorlevel 1 set error=0

cls

echo %error% > www/status.txt

cls