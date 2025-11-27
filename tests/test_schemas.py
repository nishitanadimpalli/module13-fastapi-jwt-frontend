# tests/test_schemas.py
import pytest
from pydantic import ValidationError
from app.schemas import UserCreate


def test_user_create_valid():
    user = UserCreate(
        username="nishita",
        email="test@example.com",
        password="strongpassword",
    )
    assert user.username == "nishita"
    assert user.email == "test@example.com"


def test_user_create_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="nishita",
            email="not-an-email",
            password="pass",
        )
