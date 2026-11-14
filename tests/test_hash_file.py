from src.main import hash_sha256_file,hash_sha512_file
def test_sha256_file(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hello", encoding="utf-8")
    result = hash_sha256_file(file)
    assert result == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert len(result) == 64
def test_sha512_file(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hello", encoding="utf-8")
    result = hash_sha512_file(file)
    assert len(result) == 128
    assert result == "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"