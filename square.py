def square_number(number: float) -> float:
    """
    Squares a number (second degree).

    Args:
        number (float): The number to square

    Returns:
        Float: The result of squaring

    Raises:
        TypeError: If the input parameter is not a number
    """
    if not isinstance(number, (int, float)):
        raise TypeError("The input parameter must be a number")
    return number ** 2

import unittest

class TestSquareNumber(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(square_number(2), 4)
        self.assertEqual(square_number(5), 25)
        self.assertEqual(square_number(10), 100)

    def test_negative_numbers(self):
        self.assertEqual(square_number(-2), 4)
        self.assertEqual(square_number(-5), 25)

    def test_zero(self):
        self.assertEqual(square_number(0), 0)

    def test_float_numbers(self):
        self.assertAlmostEqual(square_number(1.5), 2.25)
        self.assertAlmostEqual(square_number(-1.5), 2.25)

    def test_invalid_types(self):
        # Check that the function calls TypeError for invalid types
        with self.assertRaises(TypeError):
            square_number("2")
        with self.assertRaises(TypeError):
            square_number([1, 2, 3])
        with self.assertRaises(TypeError):
            square_number(None)
        with self.assertRaises(TypeError):
            square_number({"number": 2})

if __name__ == '__main__':
    unittest.main()
