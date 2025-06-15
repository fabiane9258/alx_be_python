import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Tests for the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Tests for the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiplication(self):
        """Tests for the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertEqual(self.calc.multiply(-3, 3), -9)

    def test_division(self):
        """Tests for the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertEqual(self.calc.divide(-8, -2), 4)

if __name__ == '__main__':
    unittest.main()
