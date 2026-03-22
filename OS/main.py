import os
import importlib
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

APPS_DIR = "apps"

# ===== TẠO Ổ G =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIRTUAL_DRIVE = os.path.join(BASE_DIR, "G")

if not os.path.exists(VIRTUAL_DRIVE):
    os.makedirs(VIRTUAL_DRIVE)


# ===== WINDOW SYSTEM =====
class Window:
    def __init__(self, parent, title):
        self.frame = tk.Frame(parent, bg="white", bd=2, relief="raised")
        self.frame.place(x=120, y=120, width=500, height=350)

        self.title_bar = tk.Frame(self.frame, bg="#245EDB", height=25)
        self.title_bar.pack(fill="x")

        tk.Label(self.title_bar, text=title, bg="#245EDB", fg="white").pack(side="left")

        tk.Button(self.title_bar, text="X", bg="red", fg="white",
                  command=self.frame.destroy).pack(side="right")

        self.content = tk.Frame(self.frame, bg="white")
        self.content.pack(fill="both", expand=True)

        self.title_bar.bind("<B1-Motion>", self.drag)

    def drag(self, event):
        x = self.frame.winfo_x() + event.x
        y = self.frame.winfo_y() + event.y
        self.frame.place(x=x, y=y)


# ===== OS =====
class PseudoOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Pseudo Windows XP")
        self.root.geometry("1000x650")

        self.apps = []

        # ===== Desktop =====
        self.desktop = tk.Frame(root, bg="#3A6EA5")
        self.desktop.pack(fill="both", expand=True)

        self.wallpaper_label = tk.Label(self.desktop)
        self.wallpaper_label.place(relwidth=1, relheight=1)
        self.wallpaper_image = None

        self.desktop.bind("<Button-3>", self.show_context_menu)

        # ===== Taskbar =====
        self.taskbar = tk.Frame(root, bg="#245EDB", height=30)
        self.taskbar.pack(side="bottom", fill="x")

        self.start_btn = tk.Button(self.taskbar, text="Start",
                                   bg="#3A6EA5", fg="white",
                                   command=self.toggle_start)
        self.start_btn.pack(side="left")

        self.start_menu = tk.Frame(root, bg="#ECE9D8", width=220)

        self.load_apps()
        self.draw_icons()
        self.draw_start_menu()

    # ===== LOAD APPS =====
    def load_apps(self):
        for file in os.listdir(APPS_DIR):
            if file.endswith(".py") and not file.startswith("__"):
                module = importlib.import_module(f"{APPS_DIR}.{file[:-3]}")
                if hasattr(module, "run"):
                    self.apps.append({
                        "name": getattr(module, "APP_NAME", file),
                        "module": module
                    })

    # ===== DESKTOP ICONS =====
    def draw_icons(self):
        for i, app in enumerate(self.apps):
            btn = tk.Button(self.desktop, text=app["name"],
                            width=14, height=2,
                            command=lambda a=app: self.open_app(a))
            btn.place(x=20, y=20 + i * 80)

    # ===== START MENU =====
    def draw_start_menu(self):
        for app in self.apps:
            tk.Button(self.start_menu,
                      text=app["name"],
                      anchor="w",
                      command=lambda a=app: self.open_app(a)).pack(fill="x")

        tk.Button(self.start_menu,
                  text="Exit",
                  bg="red", fg="white",
                  command=self.root.quit).pack(fill="x")

    def toggle_start(self):
        if self.start_menu.winfo_ismapped():
            self.start_menu.place_forget()
        else:
            self.start_menu.place(x=0, y=300)

    # ===== OPEN APP =====
    def open_app(self, app):
        win = Window(self.desktop, app["name"])

        try:
            app["module"].run(win.content, VIRTUAL_DRIVE)
        except TypeError:
            app["module"].run(win.content)

    # ===== WALLPAPER =====
    def show_context_menu(self, event):
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Change Wallpaper", command=self.change_wallpaper)
        menu.post(event.x_root, event.y_root)

    def change_wallpaper(self):
        file = filedialog.askopenfilename(filetypes=[("Image", "*.png *.jpg *.jpeg")])
        if file:
            img = Image.open(file)
            img = img.resize((1000, 650))
            self.wallpaper_image = ImageTk.PhotoImage(img)
            self.wallpaper_label.config(image=self.wallpaper_image)
            self.wallpaper_label.lower()


if __name__ == "__main__":
    root = tk.Tk()
    os_app = PseudoOS(root)
    root.mainloop()