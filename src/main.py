import hashlib
while True:
    menu = input(
    """
    HashTool choose:1
    ──────────
    2-SHA-512
    1-SHA-256
    0-Exit     
    ──────────
    :
    """)
    if menu == "0":
        break
    elif menu == "1":
        menutf = input("What do you want to hash: 1-File or 2-Text: ")
        if menutf == "1":
            file_path = input("Enter file path:")
            if not file_path.strip():
                print("File path cannot be empty!")
                continue
            try:
                with open(file_path, "rb") as file:
                    file_data = file.read()
                sha256_output_file = hashlib.sha256(file_data).hexdigest()
                print(f"SHA-256: {sha256_output_file}")
            except FileNotFoundError:
                print("File not found!")
            except PermissionError:
                print("Permission denied!")

        elif menutf == "2":
            sha256_input = input("Enter text:")
            if not sha256_input.strip():
                print("Text cannot be empty!")
                continue
            sha256_output = hashlib.sha256(sha256_input.encode()).hexdigest()
            print(sha256_output)
        else:
            print("Invalid choice!")
    elif menu == "2":
        sha512_input = input("Enter text:")
        if not sha512_input.strip():
            print("Text cannot be empty!")
            continue
        sha512_output = hashlib.sha512(sha512_input.encode()).hexdigest()
        print(sha512_output)
    else:
        print("You entered the wrong thing")