@echo off
REM === Move to the folder containing this .bat file ===
cd /d "%~dp0"

REM === Go up one folder to the project root ===
cd ..

REM === Run test.py ===
pip install -r installs.txt

pause
