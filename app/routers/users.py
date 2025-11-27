# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud_users, models, security

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# 1) Register: POST /users/register
@router.post("/register", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if username already exists
    if crud_users.get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    # Check if email already exists
    if crud_users.get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Create user (hashing happens in crud_users.create_user)
    db_user = crud_users.create_user(db, user)
    return db_user


# 2) Login: POST /users/login
@router.post("/login")
def login_user(login: schemas.UserLogin, db: Session = Depends(get_db)):
    # Find user by username
    user = crud_users.get_user_by_username(db, login.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password",
        )

    # FIXED: correct field name is password_hash
    if not security.verify_password(login.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password",
        )

    return {"message": "Login successful", "user_id": user.id}


# 3) Read user by id
@router.get("/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
