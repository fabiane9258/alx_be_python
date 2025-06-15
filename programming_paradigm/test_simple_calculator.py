import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a fresh SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- ADDITION TESTS ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -8), -11)

    def test_add_mixed_signs(self):
        self.assertEqual(self.calc.add(-5, 10), 5)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 9), 9)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- SUBTRACTION TESTS ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 7), -4)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # --- MULTIPLICATION TESTS ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(-3, 3), -9)

    # --- DIVISION TESTS ---
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_floating_point(self):
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333333333, places=6)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_negative_values(self):
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

if __name__ == '__main__':
    unittest.main()
