import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the calculator before each test."""
        self.calc = SimpleCalculator()

    # Addition Tests
    def test_addition(self):
        """Test addition of positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(10.5, 2.5), 13.0)

    # Subtraction Tests 
    def test_subtraction(self):
        """Test subtraction of positive, negative, and zero values."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(10.5, 0.5), 10.0)

    # Multiplication Tests 
    def test_multiplication(self):
        """Test multiplication of positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # Division Tests 
    def test_division(self):
        """Test normal division and division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero case

    def test_division_edge_cases(self):
        """Test edge cases for division with small or floating numbers."""
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=6)
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
