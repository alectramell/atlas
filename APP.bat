::[Bat To Exe Converter]
::
::fBE1pAF6MU+EWHreyHcjLQlHcBGROXmGIrAP4/z0/9aGtkEcR94yfYHOlKSXQA==
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFA5HSRa+GG6pDaET+NT6++aGsXEQUeY2ebPazriPM64a6UqE
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSzk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFA5HSRa+GG6pDaET+NT6++aGsXE8YM4eS8HewrHu
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
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
