import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(2.5, 0.1), 2.6)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-9, 3), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(9, 3), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

if __name__ == "__main__":
    unittest.main()
