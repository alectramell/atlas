@echo off

cls

set APPNAME=ATLAS
set APPVERS=v1.0

cls

TITLE %APPNAME% %APPVERS%

cls

python -B menu.py

cls

echo Exiting %APPNAME% %APPVERS%..
echo.
timeout /t 3 > nul
taskkill /FI "imagename eq php.exe" > nul
taskkill /FI "windowtitle eq %APPNAME% %APPVERS%" > nul
taskkill /FI "imagename eq python.exe" > nul

cls

exit
