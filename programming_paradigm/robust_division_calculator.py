# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division safely with error handling for zero and non-numeric input."""

    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
