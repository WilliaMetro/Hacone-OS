APP_NAME = "File Explorer"

import tkinter as tk
import os

def run(parent, root_path):
    listbox = tk.Listbox(parent)
    listbox.pack(fill="both", expand=True)

    current_path = [root_path]

    def load(path):
        listbox.delete(0, tk.END)
        for item in os.listdir(path):
            listbox.insert(tk.END, item)

    def open_item(event):
        selection = listbox.get(listbox.curselection())
        path = os.path.join(current_path[0], selection)

        if os.path.isdir(path):
            current_path[0] = path
            load(path)

    listbox.bind("<Double-Button-1>", open_item)

    load(root_path)