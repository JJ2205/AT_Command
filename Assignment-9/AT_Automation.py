import pyautogui
import time

# Time to switch to AT Emulator window manually
print("You have 5 seconds to focus the AT Emulator window...")
time.sleep(5)

# List of AT commands to be typed
commands = [
    "AT",
    "AT+CSQ",
    "AT+CREG?",
    "AT+CGSN",
    "AT+COPS?",
]

# Send commands one by one with a delay
for cmd in commands:
    pyautogui.write(cmd)        # Type the command
    pyautogui.press("enter")    # Press Enter
    print(f"Sent: {cmd}")
    time.sleep(1.5)             # Wait before next command
