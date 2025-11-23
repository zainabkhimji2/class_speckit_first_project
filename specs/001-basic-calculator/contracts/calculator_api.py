# contracts/calculator_api.py

"""
API contract for the Basic Calculator Library.
Defines the function signatures for supported arithmetic operations.
"""

from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers and returns their sum.

    Args:
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The sum of a and b.
    """
    pass # Implementation will be provided in src/calculator/operations.py

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts the second number from the first and returns the difference.

    Args:
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number to subtract.

    Returns:
        Union[int, float]: The difference between a and b.
    """
    pass # Implementation will be provided in src/calculator/operations.py

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers and returns their product.

    Args:
        a (Union[int, float]): The first number.
        b (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The product of a and b.
    """
    pass # Implementation will be provided in src/calculator/operations.py

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divides the first number by the second and returns the quotient.

    Args:
        a (Union[int, float]): The dividend.
        b (Union[int, float]): The divisor.

    Returns:
        Union[int, float]: The quotient of a divided by b.

    Raises:
        ZeroDivisionError: If the divisor b is zero.
    """
    pass # Implementation will be provided in src/calculator/operations.py
