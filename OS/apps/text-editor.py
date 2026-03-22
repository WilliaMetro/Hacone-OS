def run():
    print("\n=== Text Editor ===")

    text = input("Write something: ")

    with open("output.txt", "w") as f:
        f.write(text)

    print("Saved to output.txt")
    input("Press Enter to return...")
