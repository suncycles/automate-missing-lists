@echo off
REM === Move to the folder containing this .bat file ===
cd /d "%~dp0"

REM === Go up one folder to the project root ===
cd ..

REM === Move into the scripts folder ===
cd scripts

REM === Run test.py ===
python config_pointer_coords.py

pause
