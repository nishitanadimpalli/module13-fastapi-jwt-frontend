import pytest

from app.database import SessionLocal, Base, engine
from app.models import Calculation, CalculationType


# This will run ONCE before tests in this file and create tables
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)


def test_insert_calculation():
    db = SessionLocal()
    try:
        calc = Calculation(
            a=10,
            b=5,
            type=CalculationType.DIVIDE,
            result=2,
        )
        db.add(calc)
        db.commit()
        db.refresh(calc)

        assert calc.id is not None
        assert calc.result == 2
        assert calc.type == CalculationType.DIVIDE
    finally:
        db.close()
