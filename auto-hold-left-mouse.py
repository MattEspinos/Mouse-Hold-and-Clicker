import tkinter as tk
import time
import keyboard
import pyautogui
from threading import Thread

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
                # Simulate left mouse button press
                pyautogui.mouseDown(button='left', x=x, y=y)
                status_label.config(text='Auto Hold: ON')
            else:
                # Simulate left mouse button release
                pyautogui.mouseUp(button='left', x=x, y=y)
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

# Create the exit button
exit_button = tk.Button(root, text='Exit', command=exit_app)
exit_button.pack(pady=10)

# Start the toggle_hold function in a separate thread
hold_thread = Thread(target=toggle_hold)
hold_thread.daemon = True
hold_thread.start()

# Start the GUI main loop
root.mainloop()
