APP_NAME = "Text Editor"

import tkinter as tk
from tkinter import filedialog

def run(parent, root_path=None):
    text = tk.Text(parent)
    text.pack(fill="both", expand=True)

    def open_file():
        file = filedialog.askopenfilename(initialdir=root_path)
        if file:
            with open(file, "r", encoding="utf-8") as f:
                text.delete("1.0", tk.END)
                text.insert(tk.END, f.read())

    def save_file():
        file = filedialog.asksaveasfilename(initialdir=root_path)
        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(text.get("1.0", tk.END))

    menu = tk.Menu(parent)
    menu.add_command(label="Open", command=open_file)
    menu.add_command(label="Save", command=save_file)

    parent.master.master.config(menu=menu)