class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: adds two numbers without accessing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: multiplies two numbers and references a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


if __name__ == "__main__":
    # Example test to verify functionality
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
