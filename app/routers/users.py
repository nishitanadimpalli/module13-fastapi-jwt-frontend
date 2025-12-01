# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, models, security
from app.security import get_password_hash   # ✅ FIXED IMPORT

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# ======================================================
# 1) REGISTER USER
# ======================================================
@router.post("/register", response_model=schemas.UserRead)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check username already exists
    existing_username = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Check email already exists
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password correctly
    hashed_pw = get_password_hash(user.password)

    # Create new user
    new_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_pw    # ✅ FIXED FIELD NAME
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ======================================================
# 2) LOGIN USER (NOT USED — YOU USE /auth/login INSTEAD)
# ======================================================
@router.post("/login")
def login_user(login: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Kept for compatibility.
    You are using /auth/login for JWT login.
    This endpoint still works but is not needed for Module 13.
    """

    # Find by email
    user = db.query(models.User).filter(models.User.email == login.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Verify password
    if not security.verify_password(login.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful", "user_id": user.id}


# ======================================================
# 3) Get user by ID
# ======================================================
@router.get("/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
