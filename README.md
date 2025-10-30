# Missing Lists Automation Script Collection

The purpose of this collection of scripts is to automate status checking and status comparing of **FOLIO** and **ARS** items. Usage is documented below.

## Files

The file tree as follows: 

## Installs
[Python Download](https://www.python.org/downloads/)	
- Download the latest version of python from python.org. 
- When installing, make sure to check the box "Add python to PATH." 
- Run **installs.bat**
	- If this fails, ensure pip is installed. Run the python installer again and click **Modify**. Here you can see if pip is installed before running again.



## EMS Operation Instructions

**Requirements**: Able to leave the computer untouched and powered on for the duration of the search. Estimated 3 seconds per barcode. (e.x. 900 barcodes * 3sec = 2700sec, est. 45min wait)

Setup:
1. Log into EMS Control Center
2. Navigate to container management --> Inventory
3. Find Coords of buttons
7. Display filter editor and clear all other filters. Make sure the only filter is 
- **Item number: Equal:** Blank
8. Close the open filter window. Do not minimize EMS Control Center.
9. At this point, be prepared to leave the computer running and do not input any keystrokes or mouse movements. It is advised to unplug the mouse and leave the keyboard.
10. Run executables/run_ems.bat

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
1. Run executables/run_folio.bat --- *If this fails, ensure FOLIO_TOKEN.txt has the full token and is saved.*
11. Upon execution the command window will pop up. This is to monitor for any unexpected responses, however at this time it is safe to wait until the program finishes execution.
12. Upon completion the program will prompt the user for a filename. The saved json is in automate-missing-lists/results/
	--- Note: barcode order is **preserved** in the output file
13. This file is intended to be read by another script for automatic comparison.

## Comparison Instructions