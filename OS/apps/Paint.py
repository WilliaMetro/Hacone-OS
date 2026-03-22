APP_NAME = "Paint"

import tkinter as tk

def run(parent, root_path=None):
    canvas = tk.Canvas(parent, bg="white")
    canvas.pack(fill="both", expand=True)

    def draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x, y, x+3, y+3, fill="black")

    canvas.bind("<B1-Motion>", draw)