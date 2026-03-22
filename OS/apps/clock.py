APP_NAME = "Clock"

import tkinter as tk
import time

def run(root):
    window = tk.Toplevel(root)
    window.title("Clock")
    window.geometry("300x200")

    label = tk.Label(window, font=("Arial", 24))
    label.pack(pady=50)

    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        label.config(text=current_time)
        window.after(1000, update_clock)

    update_clock()