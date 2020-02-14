@echo off

cls

TITLE ATLAS v1.0

cls

python -B menu.py

cls

echo Exiting ATLAS v1.0..
echo.
timeout /t 5
taskkill /FI "imagename eq php.exe" > nul
taskkill /FI "windowtitle eq ATLAS v1.0" > nul
taskkill /FI "imagename eq python.exe" > nul

cls

exit