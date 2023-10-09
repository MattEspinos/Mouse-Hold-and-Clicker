import tkinter, customtkinter
from tkinter import messagebox
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import threading
import time


class MouseApp:
    def __init__(self, root):
        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('blue')

        self.root = root
        self.root.geometry("450x400")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure((0, 1), weight=1)
        self.root.title("Mouse App")

        self.mouse = Controller()
        self.mouse_held = {"left": False, "right": False}
        self.clicker_thread = None

        self.create_welcome_page()

        # Start a thread to listen for '=' key globally
        self.keyboard_listener_thread = threading.Thread(target=self.start_keyboard_listener, daemon=True)
        self.keyboard_listener_thread.start()

    def create_welcome_page(self):
        self.clear_frame()

        label = customtkinter.CTkLabel(self.root, text="Welcome to Mouse App!\n\nSelect an option:")
        label.grid(row=0, column=0, sticky='nsew', columnspan=2, padx=10)

        btn_hold_mouse = customtkinter.CTkButton(self.root, text="Hold Mouse", command=self.create_hold_mouse_page)
        btn_hold_mouse.grid(row=1, column=0, padx=10, pady=(0,100))

        btn_mouse_clicker = customtkinter.CTkButton(self.root, text="Mouse Clicker", command=self.create_mouse_clicker_page)
        btn_mouse_clicker.grid(row=1, column=1, padx=10, pady=(0,100))

    def create_hold_mouse_page(self):
        self.clear_frame()

        btn_back = customtkinter.CTkButton(self.root, text="Back", command=self.create_welcome_page)
        btn_back.grid(row=0, column=0, sticky='nw', padx=10)

        label = customtkinter.CTkLabel(self.root, text="Hold Mouse")
        label.grid(row=1, column=0, sticky='nsew', columnspan=2, padx=10, pady=(0, 100))

        self.var_mouse_button = customtkinter.StringVar(value="left")

        radio_left = customtkinter.CTkRadioButton(self.root, text="Left Mouse", variable=self.var_mouse_button, value="left")
        radio_left.grid(row=2, column=0, padx=5, pady=5)

        radio_right = customtkinter.CTkRadioButton(self.root, text="Right Mouse", variable=self.var_mouse_button, value="right")
        radio_right.grid(row=2, column=1, padx=5, pady=5)

        self.label_hold_status = customtkinter.CTkLabel(self.root, text="Mouse Hold Status: OFF")
        self.label_hold_status.grid(row=3, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        label_toggle_key = customtkinter.CTkLabel(self.root, text="Press '=' to toggle Mouse Hold")
        label_toggle_key.grid(row=4, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        self.root.bind('=', lambda event: self.toggle_mouse_hold())

    def create_mouse_clicker_page(self):
        self.clear_frame()
        
        btn_back = customtkinter.CTkButton(self.root, text="Back", command=self.create_welcome_page)
        btn_back.grid(row=0, column=0, sticky='nw', padx=10)

        label = customtkinter.CTkLabel(self.root, text="Mouse Clicker")
        label.grid(row=1, column=0, sticky='nsew', columnspan=2, padx=10, pady=(0, 100))

        self.var_mouse_button = customtkinter.StringVar(value="left")

        radio_left = customtkinter.CTkRadioButton(self.root, text="Left Mouse", variable=self.var_mouse_button, value="left")
        radio_left.grid(row=2, column=0, padx=5, pady=5)

        radio_right = customtkinter.CTkRadioButton(self.root, text="Right Mouse", variable=self.var_mouse_button, value="right")
        radio_right.grid(row=2, column=1, padx=5, pady=5)

        label_interval = customtkinter.CTkLabel(self.root, text="Interval (seconds):")
        label_interval.grid(row=3, column=0, padx=10, pady=10)

        combobox_var = customtkinter.StringVar(value="1")
        self.combobox_interval = customtkinter.CTkComboBox(self.root, width=100, height=30, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "45", "60"], variable=combobox_var, state='readonly')
        self.combobox_interval.grid(row=3, column=1, pady=(10,10), sticky="w")

        self.label_clicker_status = customtkinter.CTkLabel(self.root, text="Mouse Hold Status: OFF")
        self.label_clicker_status.grid(row=4, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        label_toggle_key = customtkinter.CTkLabel(self.root, text="Press '=' to toggle Mouse Hold")
        label_toggle_key.grid(row=5, column=0, sticky='nsew', columnspan=2, padx=10, pady=10)

        self.root.bind('=', lambda event: self.toggle_mouse_clicker())

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def toggle_mouse_hold(self):
        button = Button.left if self.var_mouse_button.get() == "left" else Button.right
        mouse_button = self.var_mouse_button.get()

        if self.mouse_held[mouse_button]:
            self.mouse.release(button)
            self.mouse_held[mouse_button] = False
            self.label_hold_status.configure(text=f"Mouse Hold Status: OFF")
        else:
            self.mouse.press(button)
            self.mouse_held[mouse_button] = True
            self.label_hold_status.configure(text=f"Mouse Hold Status: ON")

    def toggle_mouse_clicker(self):
        if self.clicker_thread and self.clicker_thread.is_alive():
            self.clicker_thread = None
            self.label_clicker_status.configure(text="Mouse Clicker Status: OFF")
        else:
            try:
                interval = int(self.combobox_interval.get())
                if interval <= 0:
                    raise ValueError("Interval must be a positive integer.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer for the interval.")
                return

            button = Button.left if self.var_mouse_button.get() == "left" else Button.right

            self.clicker_thread = threading.Thread(target=self.clicker_loop, args=(button, interval), daemon=True)
            self.clicker_thread.start()

            self.label_clicker_status.configure(text="Mouse Clicker Status: ON")

    def clicker_loop(self, button, interval):
        while True:
            if not self.mouse_held[self.var_mouse_button.get()]:
                self.mouse.press(button)
                time.sleep(0.1)
                self.mouse.release(button)
            time.sleep(interval)

    def start_keyboard_listener(self):
        with Listener(on_press=self.on_key_press) as listener:
            listener.join()

    def on_key_press(self, key):
        try:
            if key.char == '=':
                if self.clicker_thread:
                    self.toggle_mouse_clicker()
        except AttributeError:
            pass  # Ignore non-char key events


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = MouseApp(root)
    root.mainloop()
