import os
import importlib
import tkinter as tk
from tkinter import messagebox

APPS_DIR = "apps"

class PseudoOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Pseudo OS")
        self.root.geometry("400x300")

        self.apps = []
        self.selected_index = 0

        self.load_apps()

        self.label = tk.Label(root, text="Pseudo OS Menu", font=("Arial", 16))
        self.label.pack(pady=10)

        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(fill="both", expand=True)

        self.draw_menu()

        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Return>", self.run_selected)

    def load_apps(self):
        self.apps.clear()

        for file in os.listdir(APPS_DIR):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]
                try:
                    module = importlib.import_module(f"{APPS_DIR}.{module_name}")

                    if hasattr(module, "run"):
                        name = getattr(module, "APP_NAME", module_name)
                        self.apps.append({
                            "name": name,
                            "module": module
                        })
                except Exception as e:
                    print(f"Error loading {file}: {e}")

        # Add Exit option
        self.apps.append({"name": "Exit", "module": None})

    def draw_menu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        for i, app in enumerate(self.apps):
            if i == self.selected_index:
                bg = "blue"
                fg = "white"
            else:
                bg = "white"
                fg = "black"

            label = tk.Label(
                self.menu_frame,
                text=app["name"],
                bg=bg,
                fg=fg,
                anchor="w",
                padx=10,
                font=("Arial", 12)
            )
            label.pack(fill="x")

    def move_up(self, event):
        self.selected_index = (self.selected_index - 1) % len(self.apps)
        self.draw_menu()

    def move_down(self, event):
        self.selected_index = (self.selected_index + 1) % len(self.apps)
        self.draw_menu()

    def run_selected(self, event):
        app = self.apps[self.selected_index]

        if app["name"] == "Exit":
            self.root.quit()
            return

        try:
            app["module"].run(self.root)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    os_app = PseudoOS(root)
    root.mainloop()