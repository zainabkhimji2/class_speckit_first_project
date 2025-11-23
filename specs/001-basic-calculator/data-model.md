# Data Model for Basic Calculator Feature

**Date**: 2025-11-23

## Entities

### Number

-   **Description**: Represents any numeric input or output for calculator operations.
-   **Attributes**:
    -   `value`: The numeric value (can be an integer or a float).
-   **Type Handling**: Standard Python `int` and `float` types.

## Relationships

-   Operations (Add, Subtract, Multiply, Divide) take two `Number` entities as input and produce one `Number` entity as output.

## Validation Rules

-   Input numbers must be valid Python `int` or `float` types.
-   Division by zero is explicitly handled (raises `ZeroDivisionError`).
