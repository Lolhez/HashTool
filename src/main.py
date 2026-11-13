import hashlib
def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()
def hash_sha512(text):
    return hashlib.sha512(text.encode()).hexdigest()
def hash_sha256_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)
    return sha256.hexdigest()
if __name__ == "__main__":
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
        #SHA-256
        elif menu == "1":
            menutf = input("What do you want to hash: 1-File or 2-Text: ")
            if menutf == "1":
                file_path = input("Enter file path:")
                if not file_path.strip():
                    print("File path cannot be empty!")
                    continue
                try:
                    sha256_output_file = hash_sha256_file(file_path)
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
                sha256_output = hash_sha256(sha256_input)
                print(sha256_output)
            else:
                print("Invalid choice!")
        #SHA-512
        elif menu == "2":
            sha512_input = input("Enter text:")
            if not sha512_input.strip():
                print("Text cannot be empty!")
                continue
            sha512_output = hash_sha512(sha512_input)
            print(sha512_output)
        else:
            print("You entered the wrong thing")