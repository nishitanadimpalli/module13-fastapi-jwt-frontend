# Module 10–12 FastAPI Project  
Secure Users + Calculation CRUD + CI/CD + Docker Deployment

This project contains the work for **Module 10, 11, and Module 12** combined into a single evolving FastAPI backend.  
Each module builds on the previous one, and the final state represents all features completed up to Module 12.

---

## 🚀 Features Completed

### ✅ Module 10 — Secure User Model
- SQLAlchemy User model  
- Pydantic validation  
- Password hashing & verification  
- UserCreate and UserRead schemas  
- GitHub Actions CI for automated tests  
- Docker image pushed to Docker Hub  

---

### ✅ Module 11 — Calculation Model
- SQLAlchemy Calculation model  
- Pydantic schemas (CalculationCreate, CalculationRead)  
- Factory pattern for operations (Add, Sub, Mul, Div)  
- Unit + integration tests  
- CI/CD tests on GitHub Actions  

---

### ✅ Module 12 — User & Calculation Routes (BREAD)
- Register user → `POST /users/register`
- Login user → `POST /users/login`
- Browse calculations → `GET /calculations`
- Read calculation → `GET /calculations/{id}`
- Edit calculation → `PUT/PATCH /calculations/{id}`
- Add calculation → `POST /calculations`
- Delete calculation → `DELETE /calculations/{id}`
- All endpoints validated using Pydantic
- Full integration testing for CRUD + login
- CI/CD: Tests run → if successful → Docker image pushed automatically

---

## 🧪 Running Tests Locally

```bash
pytest -v

All tests should pass before pushing.

▶️ Running the FastAPI App
uvicorn app.main:app --reload


Open Swagger docs at:

http://127.0.0.1:8000/docs

🐳 Docker Hub Image

Your Docker Hub Repository:

https://hub.docker.com/repository/docker/nishitanadimpalli/module10-fastapi-secure-user


Pull the image using:

docker pull nishitanadimpalli/docker pull nishitanadimpalli/module10-fastapi-secure-user:latest
