import importlib

def load_app(app_name):
    try:
        module = importlib.import_module(f"apps.{app_name}")
        module.run()
    except Exception as e:
        print(f"Error loading app: {e}")
