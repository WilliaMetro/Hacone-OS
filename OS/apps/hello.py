APP_NAME = "Hello App"

import tkinter as tk

def run(root):
    window = tk.Toplevel(root)
    window.title("Hello App")
    window.geometry("300x200")

    label = tk.Label(window, text="Hello, William!", font=("Arial", 14))
    label.pack(pady=50)