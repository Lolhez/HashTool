import hashlib
while True:
    menu = input(
    """
    HashTool choose:
    ──────────
    1-SHA-256
    0-Exit     
    ──────────
    :
    """)
    if menu == "0":
        break
    elif menu == "1":
        sha256_input = input("Enter text:")
        if not sha256_input.strip():
            print("Text cannot be empty!")
            continue
        sha256_output = hashlib.sha256(sha256_input.encode()).hexdigest()
        print(sha256_output)

    else:
        print("You entered the wrong thing")