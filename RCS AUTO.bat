@echo off
cd /d "%~dp0dist"

REM Запуск программы скрыто
powershell -WindowStyle Hidden -Command "Start-Process '.\Settings.exe' -Verb runAs"