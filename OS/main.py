import os
import importlib
import tkinter as tk

APPS_DIR = "apps"

class Window:
    def __init__(self, parent, title):
        self.parent = parent

        self.frame = tk.Frame(parent, bg="white", bd=2, relief="raised")
        self.frame.place(x=100, y=100, width=300, height=200)

        # Title bar
        self.title_bar = tk.Frame(self.frame, bg="#245EDB", height=25)
        self.title_bar.pack(fill="x")

        self.title_label = tk.Label(
            self.title_bar,
            text=title,
            bg="#245EDB",
            fg="white"
        )
        self.title_label.pack(side="left", padx=5)

        self.close_btn = tk.Button(
            self.title_bar,
            text="X",
            bg="red",
            fg="white",
            command=self.close
        )
        self.close_btn.pack(side="right")

        # Content
        self.content = tk.Frame(self.frame, bg="white")
        self.content.pack(fill="both", expand=True)

        # Drag
        self.title_bar.bind("<B1-Motion>", self.drag)

    def drag(self, event):
        x = self.frame.winfo_x() + event.x
        y = self.frame.winfo_y() + event.y
        self.frame.place(x=x, y=y)

    def close(self):
        self.frame.destroy()


class PseudoOS:
    def __init__(self, root):
        self.root = root
        self.root.title("XP OS")
        self.root.geometry("800x500")

        self.apps = []

        # Desktop
        self.desktop = tk.Frame(root, bg="#3A6EA5")
        self.desktop.pack(fill="both", expand=True)

        # Taskbar
        self.taskbar = tk.Frame(root, bg="#245EDB", height=30)
        self.taskbar.pack(side="bottom", fill="x")

        self.start_btn = tk.Button(
            self.taskbar,
            text="Start",
            bg="#3A6EA5",
            fg="white",
            command=self.toggle_start
        )
        self.start_btn.pack(side="left")

        self.start_menu = tk.Frame(root, bg="#ECE9D8", width=200, height=300)

        self.load_apps()
        self.draw_desktop_icons()
        self.draw_start_menu()

    def load_apps(self):
        for file in os.listdir(APPS_DIR):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]
                module = importlib.import_module(f"{APPS_DIR}.{module_name}")

                if hasattr(module, "run"):
                    name = getattr(module, "APP_NAME", module_name)
                    self.apps.append({
                        "name": name,
                        "module": module
                    })

    # ===== Desktop Icons =====
    def draw_desktop_icons(self):
        for i, app in enumerate(self.apps):
            btn = tk.Button(
                self.desktop,
                text=app["name"],
                width=12,
                height=2,
                command=lambda a=app: self.open_app(a)
            )
            btn.place(x=20, y=20 + i * 70)

    # ===== Start Menu =====
    def draw_start_menu(self):
        for app in self.apps:
            btn = tk.Button(
                self.start_menu,
                text=app["name"],
                anchor="w",
                command=lambda a=app: self.open_app(a)
            )
            btn.pack(fill="x")

        exit_btn = tk.Button(
            self.start_menu,
            text="Exit",
            bg="red",
            fg="white",
            command=self.root.quit
        )
        exit_btn.pack(fill="x")

    def toggle_start(self):
        if self.start_menu.winfo_ismapped():
            self.start_menu.place_forget()
        else:
            self.start_menu.place(x=0, y=200)

    # ===== Open App =====
    def open_app(self, app):
        window = Window(self.desktop, app["name"])
        try:
            app["module"].run(window.content)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    os_app = PseudoOS(root)
    root.mainloop()