import tkinter as tk
import time
import ctypes
import keyboard
import pyautogui
from threading import Thread
from tkinter import messagebox

# Global variable to store the selected button (keyboard or mouse)
selected_button_type = None

# Global variable to store the keyboard character
selected_keyboard_character = None

# Global variable to track the auto-hold state
auto_hold_enabled = False

# Function to start auto-holding a keyboard button
def start_keyboard_hold():
    global selected_button_type
    selected_button_type = "keyboard"
    root.destroy()

# Function to start auto-holding a mouse button
def start_mouse_hold():
    global selected_button_type
    selected_button_type = "mouse"
    root.destroy()

# Function to toggle the auto-hold state
def toggle_auto_hold():
    global auto_hold_enabled
    auto_hold_enabled = not auto_hold_enabled

# Function to check the auto-hold state and perform the action
def auto_hold():
    global auto_hold_enabled
    while True:
        if auto_hold_enabled:
            keyboard.press(selected_keyboard_character)
        else:
            keyboard.release(selected_keyboard_character)
        time.sleep(0.1)

# Create the main window for selecting button type
root = tk.Tk()
root.title('Auto Hold Selection')

# Create labels and buttons for selecting button type
select_label = tk.Label(root, text='Select button type:', font=('Arial', 16))
select_label.pack(pady=10)

keyboard_button = tk.Button(root, text='Keyboard', command=start_keyboard_hold, font=('Arial', 12))
keyboard_button.pack(pady=5)

mouse_button = tk.Button(root, text='Mouse', command=start_mouse_hold, font=('Arial', 12))
mouse_button.pack(pady=5)

# Start the GUI main loop for button selection
root.mainloop()

# Define a list of valid keyboard keys
valid_keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'space', 'shift', 'ctrl', 'alt', 'tab', 'esc', 'enter', 'backspace',
    'insert', 'delete', 'home', 'end', 'pageup', 'pagedown', 'up', 'down',
    'left', 'right', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10',
    'f11', 'f12', '`', '-', '=', '+' '[', ']', '\\', ';', '\'', ',', '.', '/', '*'
    'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9',
]

# If "keyboard" is selected, show the keyboard input page
if selected_button_type == "keyboard":
    root = tk.Tk()
    root.title('Auto Hold - Keyboard Input')

    # Create a label for instructions
    instruct_label = tk.Label(root, text='Enter the keyboard character to auto-hold:', font=('Arial', 12))
    instruct_label.pack(pady=10)

    # Create a text entry field for keyboard character input
    keyboard_entry = tk.Entry(root, font=('Arial', 12))
    keyboard_entry.pack(pady=5)

    def next_window():
        global selected_keyboard_character
        character = keyboard_entry.get()
        
        if character and character.lower() in valid_keys:
            selected_keyboard_character = character
            root.destroy()
        else:
            messagebox.showerror("Invalid Key", "Please enter a valid keyboard character.")

    # Create a "Next" button to proceed to configuration
    next_button = tk.Button(root, text='Next', command=next_window, font=('Arial', 12))
    next_button.pack(pady=10)

    # Create the exit button
    exit_button = tk.Button(root, text='Exit', command=root.destroy)
    exit_button.pack(pady=10)

    # Start the GUI main loop for keyboard input
    root.mainloop()

# Continue to the keyboard configuration window
if selected_button_type == "keyboard" and selected_keyboard_character:
    root = tk.Tk()
    root.title('Auto Hold - Keyboard Configuration')

    # Create a label for instructions
    config_label = tk.Label(root, text=f'Auto-hold configured for key: {selected_keyboard_character}', font=('Arial', 12))
    config_label.pack(pady=10)

    # Create a toggle button for enabling/disabling auto-hold
    toggle_button_text = tk.StringVar()
    toggle_button_text.set('Enable Auto Hold')
    toggle_button = tk.Button(root, textvariable=toggle_button_text, command=toggle_auto_hold, font=('Arial', 12))
    toggle_button.pack(pady=10)

    # Create the exit button
    exit_button = tk.Button(root, text='Exit', command=root.destroy)
    exit_button.pack(pady=10)

    # Start the auto-hold thread
    auto_hold_thread = Thread(target=auto_hold, daemon=True)
    auto_hold_thread.start()

    # Start the GUI main loop for keyboard configuration
    root.mainloop()

# If "mouse" is selected or "Next" is clicked in the keyboard input window
if selected_button_type == "mouse" or selected_button_type == "keyboard_config":
    def toggle_hold():
        # Flag to keep track of the mouse button state
        is_mouse_down = False
        
        while True:
            if keyboard.is_pressed('='):
                # Toggle the mouse button state
                is_mouse_down = not is_mouse_down
                
                # Get the current mouse coordinates
                x, y = pyautogui.position()
                
                if is_mouse_down:
                    # Simulate mouse button press
                    if selected_button.get() == "Left":
                        pyautogui.mouseDown(button='left', x=x, y=y)
                    elif selected_button.get() == "Right":
                        pyautogui.mouseDown(button='right', x=x, y=y)
                    status_label.config(text=f'Auto Hold: {selected_button.get()}')
                else:
                    # Simulate mouse button release
                    if selected_button.get() == "Left":
                        pyautogui.mouseUp(button='left', x=x, y=y)
                    elif selected_button.get() == "Right":
                        pyautogui.mouseUp(button='right', x=x, y=y)
                    status_label.config(text='Auto Hold: OFF')
                
                # Delay to avoid registering multiple key presses
                time.sleep(0.2)

    def exit_app():
        root.destroy()

    # Create the main window
    root = tk.Tk()
    root.title('Auto Hold')

    # Create the status label
    status_label = tk.Label(root, text='Auto Hold: OFF', font=('Arial', 16))
    status_label.pack(pady=10)

    # Create the button description label
    button_label = tk.Label(root, text='Press "=" to toggle Auto Hold', font=('Arial', 12))
    button_label.pack(pady=5)

    # Create a radio button to select the mouse button
    selected_button = tk.StringVar(value="Left")
    left_radio = tk.Radiobutton(root, text="Left Mouse", variable=selected_button, value="Left")
    right_radio = tk.Radiobutton(root, text="Right Mouse", variable=selected_button, value="Right")
    left_radio.pack(pady=5)
    right_radio.pack(pady=5)

    # Create the exit button
    exit_button = tk.Button(root, text='Exit', command=exit_app)
    exit_button.pack(pady=10)

    # Start the toggle_hold function in a separate thread
    hold_thread = Thread(target=toggle_hold)
    hold_thread.daemon = True
    hold_thread.start()

    # Start the GUI main loop
    root.mainloop()
