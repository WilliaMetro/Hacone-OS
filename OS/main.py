from system.loader import load_app

def show_menu():
    print("\n=== FakeOS ===")
    print("1. Calculator")
    print("2. Text Editor")
    print("3. About")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Select: ")

    if choice == "1":
        load_app("calculator")
    elif choice == "2":
        load_app("text_editor")
    elif choice == "3":
        load_app("about")
    elif choice == "0":
        print("Shutting down...")
        break
    else:
        print("Invalid option!")
