# app/main.py

from fastapi import FastAPI
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

from app.database import Base, engine
from app import models
from app.routers import users, calculations, auth


# -------------------------
# 🟢 Create Database Tables
# -------------------------
Base.metadata.create_all(bind=engine)


# -------------------------
# 🟢 Initialize App
# -------------------------
app = FastAPI(
    title="FastAPI Secure User + JWT Frontend App",
    version="1.0.0",
)


# -------------------------
# 🟢 Include Routers
# -------------------------
app.include_router(users.router)         # Module 10
app.include_router(calculations.router)  # Module 12
app.include_router(auth.router)          # Module 13


# -------------------------
# 🟢 Serve Static Front-End
# -------------------------

# Folder: app/static/
static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Serve register page
@app.get("/register-page", response_class=HTMLResponse)
def register_page():
    return FileResponse(static_dir / "register.html")


# Serve login page
@app.get("/login-page", response_class=HTMLResponse)
def login_page():
    return FileResponse(static_dir / "login.html")


# -------------------------
# 🟢 Root Route
# -------------------------
@app.get("/")
def read_root():
    return {"message": "FastAPI Secure User App with JWT + Frontend is running"}
