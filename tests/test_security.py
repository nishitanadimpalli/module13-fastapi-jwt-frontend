# tests/test_security.py
from app.security import get_password_hash, verify_password


def test_password_hash_and_verify():
    raw_password = "mysecret123"
    hashed = get_password_hash(raw_password)

    assert hashed != raw_password
    assert verify_password(raw_password, hashed)
    assert not verify_password("wrongpassword", hashed)
