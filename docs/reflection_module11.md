# Module 11 Reflection

In this module, I extended my existing FastAPI user service by adding a Calculation model and additional validation logic. Defining the SQLAlchemy Calculation model made me think through which fields really belong in the database: the operands `a` and `b`, the operation `type`, and whether or not to store the `result`. I chose to store the result so that every calculation request is recorded and does not require recomputing values when the same record is retrieved later.

Working with Pydantic schemas gave me more practice with input validation. For example, I made sure that dividing by zero is blocked directly in the `CalculationCreate` schema. This keeps invalid data out of the system before it hits the database or business logic. I also learned how to serialize fields like enums and timestamps cleanly for API responses using a `CalculationRead` schema.

Implementing the calculation factory pattern was a good way to organize different operations (Add, Subtract, Multiply, Divide). Instead of using a big `if` statement everywhere, the factory returns the correct operation object, making the code easier to extend if more operations are needed later.

Finally, connecting this work to the existing CI/CD pipeline from Module 10 reinforced how everything fits together. The new unit and integration tests run automatically in GitHub Actions, and the Docker image is rebuilt and pushed to Docker Hub on success. This gave me a clear picture of how small model changes still go through a full automated process.
