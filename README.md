# Mouse-Hold-and-Clicker

Mouse-Hold-and-Clicker is a Python GUI application built using Tkinter and customtkinter. It provides two main functionalities: Hold Mouse and Mouse Clicker.

## Features

- **Hold Mouse:** Allows the user to hold down the left or right mouse button.
- **Mouse Clicker:** Lets the user automate mouse clicks at a specified interval.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `tkinter`, `customtkinter`, `pynput`, `keyboard`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MattEspinos/mouse-hold-and-clicker.git
   cd mouse-hold-and-clicker
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python mouse_hold_and_clicker.py
   ```

   **OR**

   Run the executable version:

   ```bash
   ./dist/mouse_hold_and_clicker.exe
   ```

## Usage

1. Launch the application.

2. The welcome screen presents two options: "Hold Mouse" and "Mouse Clicker."

3. **Hold Mouse:**
   - Select the mouse button to hold (left or right).
   - Press the '=' key to activate/deactivate the mouse hold.
   - Use the "Back" button to return to the welcome screen.

4. **Mouse Clicker:**
   - Select the mouse button for clicking (left or right).
   - Choose the interval for mouse clicks using the dropdown menu.
   - Press the '=' key to activate/deactivate the mouse hold.
   - Use the "Back" button to return to the welcome screen.

## Customization

- The appearance of the application can be adjusted using the `customtkinter` library.
- Modify the available intervals in the `Combobox` widget to suit your needs.

## Notes

- The application uses the '=' key to toggle both the mouse hold and mouse clicker functionalities.
- The `keyboard` library is used to capture the '=' key globally, making the application more responsive to key presses outside its window.

## Executable Version

An executable version of the application is available in the `dist` directory. Run `mouse_hold_and_clicker.exe` to use the application without Python installed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.