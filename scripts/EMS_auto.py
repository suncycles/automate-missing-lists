import pyautogui
import pyperclip
import pygetwindow as gw
import time
import pandas as pd
import json

# Init config from ems_config
def load_config(filename):
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            # Interpret edge case text, in case of user error
            line = line.strip()
            if not line or line.startswith('#'): 
                continue
            key, value = line.split('=', 1)
            value = value.strip()
            try:
                value = eval(value)
            except Exception:
                pass
            config[key.strip()] = value
    return config


config = load_config('../ems_config.txt')

# Set global variables 
APP_TITLE=config["APP_TITLE"]
BARCODES_FILE=config["BARCODES_FILE"]
OUTPUT_FILE=config["OUTPUT_FILE"]
STATUS_BOX=config["STATUS_BOX"]
FILTER_EDIT=config["FILTER_EDIT"]

# 
with open("BARCODES_FILE", "r") as f: 
        barcodes = [line.strip() for line in f if line.strip()]
results = {}

for barcode in barcodes:
    try:
        windows = gw.getWindowsWithTitle(APP_TITLE)
        if windows:
            window = windows[0]
            window.activate()  # Bring EMS to front. Does not work if window is minimized
            time.sleep(0.2)
    except Exception as e:
        print(f"Could not focus window: {e}")
    
    pyautogui.moveTo(FILTER_EDIT)# Click at Filter Editor Coords
    time.sleep(0.1)
    pyautogui.click()
        
    # Navigate to barcode entry
    pyautogui.press('tab')    
    pyautogui.press('tab')
    pyautogui.press('backspace')
    time.sleep(0.1)  
    
    # Write new barcode
    try:
        if barcode != "NULL":
            barcode = int(barcode)
    except Exception as e:
        pyperclip.copy(f"{barcode}: Missing from ARS")
        
    pyautogui.write(str(barcode), interval=0.01)
    time.sleep(0.2)  
    
    # Press OK
    ok_loc = pyautogui.locateOnScreen('detection_imgs/ok_button.png', confidence=0.9)
    time.sleep(0.1)  
    
    pyautogui.click(ok_loc)
    time.sleep(0.5)  
    # Copy and Paste status box
    pyautogui.moveTo(STATUS_BOX)    
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')    
    status = pyperclip.paste()
    
    # Log results
    results[barcode] = status
    
    time.sleep(0.5)  
    
# Save results
with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=4)
    

