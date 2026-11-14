import hashlib
def hash_text(text, algorithm):
    hash_algorithm = hashlib.new(algorithm)
    hash_algorithm.update(text.encode())
    return hash_algorithm.hexdigest()
def hash_file(file_path, algorithm):
    hashfile_algorithm = hashlib.new(algorithm)
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hashfile_algorithm.update(chunk)
    return hashfile_algorithm.hexdigest()
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
            menutf256 = input("What do you want to hash: 1-File or 2-Text: ")
            if menutf256 == "1":
                file_path = input("Enter file path:")
                if not file_path.strip():
                    print("File path cannot be empty!")
                    continue
                try:
                    sha256_output_file = hash_file(file_path,"sha256")
                    print(f"SHA-256: {sha256_output_file}")
                except FileNotFoundError:
                    print("File not found!")
                except PermissionError:
                    print("Permission denied!")

            elif menutf256 == "2":
                sha256_input = input("Enter text:")
                if not sha256_input.strip():
                    print("Text cannot be empty!")
                    continue
                sha256_output = hash_text(sha256_input,"sha256")
                print(sha256_output)
            else:
                print("Invalid choice!")
        #SHA-512
        elif menu == "2":
            menutf512 = input("What do you want to hash: 1-File or 2-Text: ")
            if menutf512 == "1":
                file_path = input("Enter file path:")
                if not file_path.strip():
                    print("File path cannot be empty!")
                    continue
                try:
                    sha512_output_file = hash_file(file_path,"sha512")
                    print(f"SHA-512: {sha512_output_file}")
                except FileNotFoundError:
                    print("File not found!")
                except PermissionError:
                    print("Permission denied!")
            elif menutf512 == "2":
                sha512_input = input("Enter text:")
                if not sha512_input.strip():
                    print("Text cannot be empty!")
                    continue
                sha512_output = hash_text(sha512_input,"sha512")
                print(sha512_output)
            else:
                print("Invalid choice!")
        else:
            print("You entered the wrong thing")