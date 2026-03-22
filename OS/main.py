import os
import importlib
import tkinter as tk

APPS_DIR = "apps"

class PseudoOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Pseudo OS - XP Style")
        self.root.geometry("600x400")
        self.root.configure(bg="#3A6EA5")  # nền xanh XP

        self.apps = []
        self.selected_index = 0

        self.load_apps()

        # ===== Desktop Area =====
        self.desktop = tk.Frame(root, bg="#3A6EA5")
        self.desktop.pack(fill="both", expand=True)

        # ===== Menu =====
        self.menu_frame = tk.Frame(self.desktop, bg="#ECE9D8", width=200)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self.desktop, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # ===== Taskbar =====
        self.taskbar = tk.Frame(root, bg="#245EDB", height=30)
        self.taskbar.pack(side="bottom", fill="x")

        self.task_label = tk.Label(
            self.taskbar,
            text="Start",
            bg="#245EDB",
            fg="white"
        )
        self.task_label.pack(side="left", padx=10)

        self.draw_menu()

        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Return>", self.run_selected)

    def load_apps(self):
        self.apps.clear()

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

        self.apps.append({"name": "Exit", "module": None})

    def draw_menu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        for i, app in enumerate(self.apps):
            if i == self.selected_index:
                bg = "#316AC5"
                fg = "white"
            else:
                bg = "#ECE9D8"
                fg = "black"

            label = tk.Label(
                self.menu_frame,
                text=app["name"],
                bg=bg,
                fg=fg,
                anchor="w",
                padx=10,
                pady=5
            )
            label.pack(fill="x")

    def move_up(self, event):
        self.selected_index = (self.selected_index - 1) % len(self.apps)
        self.draw_menu()

    def move_down(self, event):
        self.selected_index = (self.selected_index + 1) % len(self.apps)
        self.draw_menu()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def run_selected(self, event):
        app = self.apps[self.selected_index]

        if app["name"] == "Exit":
            self.root.quit()
            return

        self.clear_content()

        try:
            # truyền content_frame thay vì root
            app["module"].run(self.content_frame)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    os_app = PseudoOS(root)
    root.mainloop()