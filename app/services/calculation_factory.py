from app.models import CalculationType


class AddOperation:
    def calculate(self, a, b):
        return a + b


class SubOperation:
    def calculate(self, a, b):
        return a - b


class MultiplyOperation:
    def calculate(self, a, b):
        return a * b


class DivideOperation:
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class CalculationFactory:
    @staticmethod
    def create_operation(operation_type):
        if operation_type == CalculationType.ADD:
            return AddOperation()
        if operation_type == CalculationType.SUB:
            return SubOperation()
        if operation_type == CalculationType.MULTIPLY:
            return MultiplyOperation()
        if operation_type == CalculationType.DIVIDE:
            return DivideOperation()
        raise ValueError("Invalid calculation type")
