# Auto Hold

Auto Hold is a Python program that allows you to automate key holding for keyboard keys. It provides an easy-to-use graphical user interface (GUI) for selecting a key to hold down and toggling the auto-hold feature on and off.

**Note**: An executable version of this program is available for users who don't have Python installed.

## Features

- **Keyboard and Mouse Options**: Choose between holding down a keyboard key or a mouse button.

- **Efficient Auto-Hold**: The program efficiently manages key holding without causing significant CPU usage.

- **Error Handling**: If you enter an invalid key, the program will display an error message, prompting you to enter a valid keyboard character.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **For Python Version**:
  - Python 3.x installed on your system.
  - Required Python packages installed. You can install them using the provided `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```

- **For Executable Version**:
  - No Python installation is required.

## Usage

1. **Python Version**:
   - Run the program by executing the `auto_hold.py` script.

2. **Executable Version**:
   - Download the executable version of the program for your operating system from the [Releases](https://github.com/MattEspinos/releases) section of this repository.

3. **Common Steps for Both Versions**:
   - The main window will appear, allowing you to choose between keyboard and mouse options.

   - If you select the keyboard option:
     - Enter a keyboard character (except '=') in the input field.
     - Click the "Next" button.
     - In the configuration window, you can toggle the auto-hold feature on and off by clicking the "Enable Auto Hold" button.

   - If you select the mouse option, the program will auto-hold the left mouse button. Click the "=" key to toggle the auto-hold feature on and off.

   - To exit the program, click the "Exit" button in any window.

## Troubleshooting

- **Performance Issues**: If the program causes significant PC slowdowns, consider closing other resource-intensive applications or tasks running on your system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [keyboard](https://github.com/boppreh/keyboard): A Python library for working with keyboards.
- [pyautogui](https://pyautogui.readthedocs.io/): A Python library for GUI automation.

## Support

For any issues or questions, please feel free to open an issue in this repository.