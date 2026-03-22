APP_NAME = "Clock"

import tkinter as tk
import time

def run(parent):
    label = tk.Label(parent, font=("Arial", 24))
    label.pack(pady=50)

    def update():
        label.config(text=time.strftime("%H:%M:%S"))
        parent.after(1000, update)

    update()