# Quickstart Guide: Basic Calculator Library

**Date**: 2025-11-23

## Installation

```bash
pip install your-calculator-library # Placeholder: Replace with actual installation command
```

## Usage

### Addition

```python
from your_calculator_library import add

result = add(10, 5)
print(f"10 + 5 = {result}") # Expected: 15

result_float = add(2.5, 1.5)
print(f"2.5 + 1.5 = {result_float}") # Expected: 4.0
```

### Subtraction

```python
from your_calculator_library import subtract

result = subtract(10, 5)
print(f"10 - 5 = {result}") # Expected: 5
```

### Multiplication

```python
from your_calculator_library import multiply

result = multiply(10, 5)
print(f"10 * 5 = {result}") # Expected: 50
```

### Division

```python
from your_calculator_library import divide

result = divide(10, 5)
print(f"10 / 5 = {result}") # Expected: 2.0

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}") # Expected: Error: division by zero
```

## Notes

- Replace `your-calculator-library` with the actual package name once defined.
- The examples demonstrate basic usage; refer to the full API documentation for more details.
