## Simple-Keylogger

### Keylogger for Linux and Windows

### Project Description
This project is a basic keylogger for both Linux and Windows systems, written in Python. It uses the `pyxhook` library for Linux and `pynput` for Windows to capture and log keyboard inputs, storing the log in a file. The keylogger is useful for ethical hacking, security testing, or monitoring purposes.

## Features
- Captures and logs all keypresses.
- Logs keys like Space, Enter, Tab, and Backspace with corresponding labels.
- Saves the log to a file, which can be customized.
- Simple to set up and run.
- Cancel key to stop logging (`` ` `` for Linux, `Esc` for Windows by default).

## Installation Instructions
### For Linux
- Install the necessary library: `pip install pyxhook`
- Clone the repository:
`git clone https://github.com/saidheeraj22084/Simple-Keylogger.git`
`cd Keylogger-Linux`
- Run the keylogger: `python keylogger_linux.py`
- View the log file:
- Open the log file located at `~/Desktop/file.log` or the path you've set in the environment variable
### For Windows
- Install the necessary library: `pip install pynput`
- Clone the repository:
`git clone https://github.com/saidheeraj22084/Simple-Keylogger.git`
`cd Keylogger-Windows`
- Run the keylogger: `python keylogger_windows.py`
- View the log file:
- Open the log file located at `~/Desktop/file.log` or the path you've set in the environment variable

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
