# Mouse App

Mouse App is a Python GUI application built using Tkinter and customtkinter. It allows users to perform two main actions: Hold Mouse and Mouse Clicker.

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
   git clone https://github.com/your-username/mouse-app.git
   cd mouse-app
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python mouse_app.py
   ```

## Usage

1. Launch the application.

2. The welcome screen presents two options: "Hold Mouse" and "Mouse Clicker."

3. **Hold Mouse:**
   - Select the mouse button to hold (left or right).
   - Click the "Press '=' to toggle Mouse Hold" label to activate/deactivate the mouse hold.
   - Use the "Back" button to return to the welcome screen.

4. **Mouse Clicker:**
   - Select the mouse button for clicking (left or right).
   - Choose the interval for mouse clicks using the dropdown menu.
   - Click the "Press '=' to toggle Mouse Clicker" label to start/stop the mouse clicker.
   - Use the "Back" button to return to the welcome screen.

## Customization

- The appearance of the application can be adjusted using the `customtkinter` library.
- Modify the available intervals in the `Combobox` widget to suit your needs.

## Notes

- The application uses the '=' key to toggle both the mouse hold and mouse clicker functionalities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
