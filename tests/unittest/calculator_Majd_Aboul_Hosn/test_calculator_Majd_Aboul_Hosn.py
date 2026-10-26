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

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 2), 0)
        self.assertEqual(modulus(-10, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
