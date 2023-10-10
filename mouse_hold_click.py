import tkinter, customtkinter, keyboard
from tkinter import messagebox
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener
import threading
import time
import sys

class MouseApp:
    def __init__(self, root):
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('blue')

        self.root = root
        self.root.geometry("450x400")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure((0, 1), weight=1)
        self.root.title("Mouse Hold and Clicker")

        self.mouse = Controller()
        self.mouse_held = {"left": False, "right": False}
        self.clicker_running = False
        self.clicker_thread = None

        self.create_welcome_page()

        # Start a thread to listen for '=' key globally
        self.keyboard_listener_thread = threading.Thread(target=self.start_keyboard_listener, daemon=True)
        self.keyboard_listener_thread.start()

    def create_welcome_page(self):
        self.clear_frame()

        label = customtkinter.CTkLabel(self.root, text="Welcome to the Mouse Hold and Clicker App!\n\nSelect an option:", font=(None, 18))
        label.grid(row=0, column=0, sticky='nsew', columnspan=2, padx=10)

        btn_hold_mouse = customtkinter.CTkButton(self.root, text="Hold Mouse", command=self.create_hold_mouse_page)
        btn_hold_mouse.grid(row=1, column=0, padx=10, pady=(0,100))

        btn_mouse_clicker = customtkinter.CTkButton(self.root, text="Mouse Clicker", command=self.create_mouse_clicker_page)
        btn_mouse_clicker.grid(row=1, column=1, padx=10, pady=(0,100))

    def create_hold_mouse_page(self):
        self.clear_frame()

        self.in_hold_page = True
        self.in_clicker_page = False

        btn_back = customtkinter.CTkButton(self.root, text="Back", command=self.create_welcome_page)
        btn_back.grid(row=0, column=0, sticky='nw', padx=10)

        label = customtkinter.CTkLabel(self.root, text="Hold Mouse", font=(None, 20))
        label.grid(row=1, column=0, sticky='nsew', columnspan=2, padx=10, pady=(0, 100))

        self.var_mouse_button = customtkinter.StringVar(value="left")

        radio_left = customtkinter.CTkRadioButton(self.root, text="Left Mouse", variable=self.var_mouse_button, value="left")
        radio_left.grid(row=2, column=0, padx=5, pady=5)

        radio_right = customtkinter.CTkRadioButton(self.root, text="Right Mouse", variable=self.var_mouse_button, value="right")
        radio_right.grid(row=2, column=1, padx=5, pady=5)

        self.label_hold_status = customtkinter.CTkLabel(self.root, text="Mouse Hold Status: OFF", font=(None, 18), text_color='lightblue')
        self.label_hold_status.grid(row=3, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        label_toggle_key = customtkinter.CTkLabel(self.root, text="Press '=' to toggle Mouse Hold")
        label_toggle_key.grid(row=4, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        # Use keyboard library to listen for key events globally
        keyboard.on_press_key('=', lambda event: self.toggle_mouse_hold())
        keyboard.on_press_key('-', lambda event: self.close_program())

    def create_mouse_clicker_page(self):
        self.clear_frame()

        self.in_hold_page = False
        self.in_clicker_page = True

        btn_back = customtkinter.CTkButton(self.root, text="Back", command=self.create_welcome_page)
        btn_back.grid(row=0, column=0, sticky='nw', padx=10)

        label = customtkinter.CTkLabel(self.root, text="Mouse Clicker", font=(None, 20))
        label.grid(row=1, column=0, sticky='nsew', columnspan=2, padx=10, pady=(0, 100))

        self.var_mouse_button = customtkinter.StringVar(value="left")

        radio_left = customtkinter.CTkRadioButton(self.root, text="Left Mouse", variable=self.var_mouse_button, value="left")
        radio_left.grid(row=2, column=0, padx=5, pady=5)

        radio_right = customtkinter.CTkRadioButton(self.root, text="Right Mouse", variable=self.var_mouse_button, value="right")
        radio_right.grid(row=2, column=1, padx=5, pady=5)

        label_interval = customtkinter.CTkLabel(self.root, text="Interval (seconds):")
        label_interval.grid(row=3, column=0, padx=10, pady=10)

        combobox_var = customtkinter.StringVar(value="1")
        self.combobox_interval = customtkinter.CTkComboBox(self.root, width=100, height=30, values=["0.1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60"], variable=combobox_var, state='readonly')
        self.combobox_interval.grid(row=3, column=1, pady=(10,10), sticky="w")

        self.label_clicker_status = customtkinter.CTkLabel(self.root, text="Mouse Clicker Status: OFF", font=(None, 18), text_color='lightblue')
        self.label_clicker_status.grid(row=4, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        label_toggle_key = customtkinter.CTkLabel(self.root, text="Press '=' to toggle Mouse Clicker")
        label_toggle_key.grid(row=5, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        # Use keyboard library to listen for key events globally
        keyboard.on_press_key('=', lambda event: self.toggle_mouse_clicker())
        keyboard.on_press_key('-', lambda event: self.close_program())

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def toggle_mouse_hold(self):
        if self.in_hold_page:
            button = Button.left if self.var_mouse_button.get() == "left" else Button.right
            mouse_button = self.var_mouse_button.get()

            if self.mouse_held[mouse_button]:
                self.mouse.release(button)
                self.mouse_held[mouse_button] = False
                self.label_hold_status.configure(text=f"Mouse Hold Status: OFF", text_color='lightblue')
            else:
                self.mouse.press(button)
                self.mouse_held[mouse_button] = True
                self.label_hold_status.configure(text=f"Mouse Hold Status: ON", text_color='red')

    def toggle_mouse_clicker(self):
        if self.clicker_thread and self.clicker_thread.is_alive():
            self.clicker_running = False
            self.clicker_thread.join()  # Wait for the thread to finish
            self.clicker_thread = None
            self.label_clicker_status.configure(text="Mouse Clicker Status: OFF", text_color='lightblue')
        elif self.in_clicker_page:
            try:
                interval = float(self.combobox_interval.get())
                if interval <= 0:
                    raise ValueError("Interval must be a positive number.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive number for the interval.")
                return

            button = Button.left if self.var_mouse_button.get() == "left" else Button.right

            self.clicker_running = True
            self.clicker_thread = threading.Thread(target=self.clicker_loop, args=(button, interval), daemon=True)
            self.clicker_thread.start()

            self.label_clicker_status.configure(text="Mouse Clicker Status: ON", text_color='red')


    def clicker_loop(self, button, interval):
        while self.clicker_running:
            if not self.mouse_held[self.var_mouse_button.get()]:
                self.mouse.click(button, 1)  # Click once
            time.sleep(interval)


    def start_keyboard_listener(self):
        with Listener(on_press=self.on_key_press) as listener:
            listener.join()

    def on_key_press(self, key):
        try:
            if key.char == '=':
                if self.in_clicker_page:
                    self.toggle_mouse_clicker()
            elif key.char == '-':
                self.close_program()
        except AttributeError:
            pass  # Ignore non-char key events

    def close_program(self):
        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = MouseApp(root)
    root.mainloop()
