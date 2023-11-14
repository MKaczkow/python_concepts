import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(1, -1), 2)
        self.assertEqual(calc.subtract(-3, -3), -0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, -1), -1)
        self.assertEqual(calc.multiply(-3, -3), 9)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-3, -3), 1)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
