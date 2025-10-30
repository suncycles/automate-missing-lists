@echo off
REM === Move to the folder containing this .bat file ===
cd /d "%~dp0"

REM === Go up one folder to the project root ===
cd ..

REM === Move into the scripts folder ===
cd scripts

REM === Set the base path for results ===
set "RESULTS_PATH=..\results\"

REM === Prompt user for filenames ===
echo Enter the FOLIO search file to compare (e.g. FOLIO_firstSearch.json):
set /p FILE1=
echo Enter the EMS search file to compare (e.g. EMS_firstSearch.json):
set /p FILE2=

REM === Prepend the ../results/ path ===
set "FILE1=%RESULTS_PATH%%FILE1%"
set "FILE2=%RESULTS_PATH%%FILE2%"

REM === Run the Python script with those full paths ===
python compare_status.py "%FILE1%" "%FILE2%"

pause
