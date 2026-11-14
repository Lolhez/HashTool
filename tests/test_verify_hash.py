from  src.main import verify_file_hash

def test_verify_correct_hash(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hello", encoding="utf-8")

    expected_hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

    result = verify_file_hash(file, expected_hash, "sha256")

    assert result is True


def test_verify_wrong_hash(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hello", encoding="utf-8")
    expected_hash = "9b71d224bd6"
    result = verify_file_hash(file, expected_hash, "sha256")
    assert result is False


