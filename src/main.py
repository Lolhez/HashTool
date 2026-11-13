import hashlib
while True:
    menu = input(
    """
    HashTool choose:
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
        sha256_input = input("Enter text:")
        if not sha256_input.strip():
            print("Text cannot be empty!")
            continue
        sha256_output = hashlib.sha256(sha256_input.encode()).hexdigest()
        print(sha256_output)
    elif menu == "2":
        sha512_input = input("Enter text:")
        if not sha512_input.strip():
            print("Text cannot be empty!")
            continue
        sha512_output = hashlib.sha512(sha512_input.encode()).hexdigest()
        print(sha512_output)
    else:
        print("You entered the wrong thing")