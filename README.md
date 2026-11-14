# HashTool

A simple command-line tool written in Python for generating and verifying cryptographic hashes.

## Features

- Generate SHA-256 and SHA-512 hashes
- Hash text and files
- Verify file integrity by comparing hashes
- Process large files in chunks
- Handle common file errors
- Interactive CLI menu

## Technologies

- Python 3
- hashlib (Python standard library)
- pytest (automated testing)

## Installation

Clone the repository:

```bash
git clone https://github.com/Lolhez/HashTool.git
cd HashTool
```

## Usage

Run the application:

```bash
python -m src.main
```

Choose an option from the menu:

```text
HashTool choose:
--------------------
3 - Verify File Hash
2 - SHA-512
1 - SHA-256
0 - Exit
--------------------
```

## Running Tests

Install pytest:

```bash
python -m pip install pytest
```

Run all tests:

```bash
python -m pytest -v
```

## How File Verification Works

1. Select the verification option.
2. Choose SHA-256 or SHA-512.
3. Enter the file path.
4. Enter the expected hash.
5. HashTool calculates the file hash and compares it with the expected value.

If the hashes match, the file passes verification.

## Author

Developed by [Lolhez](https://github.com/Lolhez).

## Version

1.0.0