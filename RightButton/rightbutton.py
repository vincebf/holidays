import pyautogui
import time
import sys


position = pyautogui.position()
print("当前鼠标位置:", position.x, position.y)

# Configuration
CLICK_INTERVAL = 25  # seconds between clicks
TARGET_X = 954  # X coordinate on screen
TARGET_Y = 721  # Y coordinate on screen


def main():
    print("Starting auto-clicker. Press Ctrl+C to stop.")
    try:
        while True:
            pyautogui.click(x=TARGET_X, y=TARGET_Y)
            time.sleep(CLICK_INTERVAL)
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")


if __name__ == "__main__":
    main()
