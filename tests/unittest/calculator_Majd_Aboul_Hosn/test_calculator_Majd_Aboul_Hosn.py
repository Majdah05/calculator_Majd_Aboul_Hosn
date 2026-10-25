import sys
import unittest
from pathlib import Path

# Allow the tests to run directly without installing the calculator package.
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src/main/python"))

from calculator_Majd_Aboul_Hosn import (
    add, subtract, multiply, divide, modulus, power, square_root,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_and_zero(self):
        self.assertEqual(add(-3, 2), -1)
        self.assertEqual(add(0, 0), 0)

    def test_add_decimals(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_and_zero(self):
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-3, -5), 2)
        self.assertEqual(subtract(4, 4), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_and_zero(self):
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_negative_and_zero_numerator(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)

    def test_modulus_negative_and_zero(self):
        self.assertEqual(modulus(-10, 3), 2)
        self.assertEqual(modulus(10, -3), -2)
        self.assertEqual(modulus(0, 3), 0)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)

    def test_power_zero(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 3), 0)
        self.assertEqual(power(0, 0), 1)

    def test_power_negative_and_fractional_exponent(self):
        self.assertEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(9, 0.5), 3)

    def test_power_zero_to_negative_exponent(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_zero_and_fraction(self):
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(0.25), 0.5)

    def test_square_root_non_perfect_square(self):
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
