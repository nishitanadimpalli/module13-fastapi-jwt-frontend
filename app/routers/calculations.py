# app/routers/calculations.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.services.calculation_factory import CalculationFactory

router = APIRouter(
    prefix="/calculations",
    tags=["calculations"],
)


# ⭐ 1) CREATE calculation
@router.post("/", response_model=schemas.CalculationRead, status_code=status.HTTP_201_CREATED)
def create_calculation(calc: schemas.CalculationCreate, db: Session = Depends(get_db)):

    # Use factory to compute result
    result = CalculationFactory.create_operation(calc.type).calculate(calc.a, calc.b)

    db_calc = models.Calculation(
        a=calc.a,
        b=calc.b,
        type=calc.type,
        result=result
    )

    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)

    return db_calc


# ⭐ 2) BROWSE all calculations
@router.get("/", response_model=list[schemas.CalculationRead])
def get_calculations(db: Session = Depends(get_db)):
    return db.query(models.Calculation).all()


# ⭐ 3) READ one calculation (by ID)
@router.get("/{calc_id}", response_model=schemas.CalculationRead)
def get_calculation(calc_id: int, db: Session = Depends(get_db)):
    calc = db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")
    return calc


# ⭐ 4) EDIT calculation (PUT)
@router.put("/{calc_id}", response_model=schemas.CalculationRead)
def update_calculation(calc_id: int, update: schemas.CalculationCreate, db: Session = Depends(get_db)):

    calc = db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    # recompute using factory
    new_result = CalculationFactory.create_operation(update.type).calculate(update.a, update.b)

    calc.a = update.a
    calc.b = update.b
    calc.type = update.type
    calc.result = new_result

    db.commit()
    db.refresh(calc)
    return calc


# ⭐ 5) DELETE calculation
@router.delete("/{calc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_calculation(calc_id: int, db: Session = Depends(get_db)):

    calc = db.query(models.Calculation).filter(models.Calculation.id == calc_id).first()
    if not calc:
        raise HTTPException(status_code=404, detail="Calculation not found")

    db.delete(calc)
    db.commit()

    return {"message": "Deleted successfully"}
