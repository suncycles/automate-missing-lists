# Missing Lists Automation Script Collection

The purpose of this collection of scripts is to automate status checking and status comparing of **FOLIO** and **ARS** items. Usage is documented below.

## Files

The file tree as follows: 

automate missing lists/
    ├── executables/
    │   ├── coords.bat
    │   ├── installs.bat
    │   ├── run_comparison.bat
    │   ├── run_ems.bat
    │   └── run_folio.bat
    ├── results/
    │   ├── # Your search results will go here
    │   ├── e.g. firstSearch_EMS.json
    │   └── e.g. firstSearch_FOLIO.json
    ├── scripts/
    │   ├── detection_imgs/
    │   │   └── ok_button.png
    │   ├── compare_status.py
    │   ├── config_pointer_coords.py
    │   ├── EMS_auto.py
    │   └── FOLIO_request.py
    ├── barcodes.txt #INPUT FILE
    ├── config_ems_coords.png
    ├── config_token_location.png
    ├── ems_config.txt
    ├── FOLIO_TOKEN.txt
    ├── installs.txt
    ├── README.md
    └── results.csv #OUTPUT FILE



## Installs
[Python Download](https://www.python.org/downloads/)	
- Download the latest version of python from python.org. 
- When installing, make sure to check the box "Add python to PATH." 
- Run **/executables/installs.bat**
	- If this fails, ensure pip is installed. Run the python installer again and click **Modify**. Here you can see if pip is installed before running again.

## Setup
- Paste barcodes into barcodes.txt. It is intended to read them as a column, pasted directly from a spreadsheet. Do not include a heading column title. 

## FOLIO Operation Instructions
**Requirements**: Working log in to SCU  [FOLIO](https://scu.folio.indexdata.com/)

Setup:
1. Log into FOLIO using Google Chrome (Layout may differ if not on Chrome)
2. Navigate into automate-missing-lists/FOLIO folder
3. Right click when in Folio and pick *Inspect Element*. The keyboard shortcut for this is F12 on most systems.
4. The inspect window will have a bar at the very top with "Elements", "Console", "Sources", "Network", etc.
5. Navigate to "Application" tab
6. Refresh the page
7. Locate 'folioAccessToken' and copy the VALUE field
8. **For any trouble locating the access token, refer to *config_token_location.png***
9. Paste the value into **FOLIO_TOKEN.txt** and save the file.

Usage:
1. Run **executables/run_folio.bat** --- *If this fails, ensure FOLIO_TOKEN.txt has the full token and is saved.*
11. Upon execution the command window will pop up. This is to monitor for any unexpected responses, however at this time it is safe to wait until the program finishes execution.
12. Upon completion the program will prompt the user for a filename. The saved json is in /results/
	--- Note: barcode order is **preserved** in the output file
13. This file is intended to be read by another script for automatic comparison.

## EMS Operation Instructions

**Requirements**: Able to leave the computer untouched and powered on for the duration of the search. Estimated 3 seconds per barcode. (e.x. 900 barcodes * 3sec = 2700sec, est. 45min wait)

Setup:
1. Log into EMS Control Center
2. Navigate to container management --> Inventory
3. Display filter editor and clear all other filters. Make sure the only filter is **Item number: Equal:** Blank
4. Close the open filter window. Do not minimize EMS Control Center.
5. We need to find the on-screen coordinates of "Display Filter Editor" button, and Circulation Status Column Entry.
- Open config_ems_coords.png for reference
6. Run **/executables/coords.bat.** Write down the coordinates found. 
7. Enter them into **ems_config.txt** under STATUS_BOX and FILTER_EDIT.
8. Optionally, configure the OUTPUT_FILE to something else.
9. At this point, be prepared to leave the computer running and do not input any keystrokes or mouse movements. It is advised to unplug the mouse and leave the keyboard.
10. Run **/executables/run_ems.bat**
--- Note: barcode order is **preserved** in the output file
11. This file is intended to be read by another script for automatic comparison.



## Comparison Instructions
1. Run **/executables/run_comparison.bat**
2. Follow the instructions on screen
3. results are written to results.csv. This should be opened in Excel. It includes columns Item ID, FOLIO Status, EMS Status, Comparison Result.


## Notes
- EMS search will fail if the Window name of EMS control center is changed. The EMS config file  has this configurable in case it changes.
- EMS search relies on computer vision to  find the OK button after entering a barcode in the filter editor. If the button looks different than the one in scripts/detection_imgs/, replace ok_button.png with the new one.
- FOLIO token will change with each new session (Login), so token will have to be reconfigured for each new session.


