from src.main import hash_sha256_file
def test_sha256_file(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hello", encoding="utf-8")
    result = hash_sha256_file(file)
    assert result == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert len(result) == 64