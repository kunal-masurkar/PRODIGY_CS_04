# Simple Keylogger (For Ethical Use)

A basic Python keylogger for educational and ethical use only. This tool demonstrates how keystrokes can be captured and logged to a local file. **Explicit user permission is mandatory before running this tool.**

## Features
- **Logs Keystrokes:** Captures all key presses and saves them to a local file (`keylog.txt`).
- **Easy to Start/Stop:** Logging can be stopped at any time by pressing the `Esc` key.
- **Ethical Use:** Prompts for user consent before starting.
- **Timestamped Logs:** Each keystroke is logged with a timestamp.

## Requirements
- Python 3.x
- [pynput](https://pypi.org/project/pynput/) library for keyboard event capture

Install `pynput` with:
```bash
pip install pynput
```

## Usage
1. Run the script:
    ```bash
    python keylogger.py
    ```
2. When prompted, confirm you have permission to run the tool.
3. Keystrokes will be logged to `keylog.txt` in the script's directory.
4. Press the `Esc` key to stop logging and exit the program.

## Ethical Notice
> **This tool is for educational and ethical use only. Unauthorized keylogging is illegal and unethical. Always obtain explicit, written permission from the device owner before running this tool.**

---
*Created as part of the Prodigy InfoTech internship tasks.* 
