import pyautogui
import time

print("=" * 50)
print("COORDINATE FINDER")
print("=" * 50)
print("\nMove your mouse over the status text area and View Filter Editor.")
print("Write down the X and Y values")
print("Press Ctrl+C to stop\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x:4d}  Y: {y:4d}  |  Position: ({x}, {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n\nStopped!")