import pytest
from app.models import CalculationType
from app.schemas import CalculationCreate
from app.services.calculation_factory import CalculationFactory


def test_add():
    op = CalculationFactory.get_operation(CalculationType.ADD)
    assert op.compute(2, 3) == 5


def test_sub():
    op = CalculationFactory.get_operation(CalculationType.SUB)
    assert op.compute(5, 3) == 2


def test_multiply():
    op = CalculationFactory.get_operation(CalculationType.MULTIPLY)
    assert op.compute(4, 3) == 12


def test_divide():
    op = CalculationFactory.get_operation(CalculationType.DIVIDE)
    assert op.compute(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        op = CalculationFactory.get_operation(CalculationType.DIVIDE)
        op.compute(10, 0)


def test_pydantic_divide_by_zero():
    with pytest.raises(ValueError):
        CalculationCreate(a=5, b=0, type=CalculationType.DIVIDE)
