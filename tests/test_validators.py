from src.validators import is_valid_email
def test_valid_email():
    assert is_valid_email("a@b.com") is True
