def run():
    print("\n=== Calculator ===")

    try:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))
        print("Result:", a + b)
    except:
        print("Invalid input")

    input("Press Enter to return...")
