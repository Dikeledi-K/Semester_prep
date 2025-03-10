import unittest

class MyTestCases(unittest.TestCase):

    def test_check_number_odd_number(self):
        """Test case for an odd number."""
        self.assertEqual(3 % 2, 1)  # Example: 3 is odd

    def test_check_number_even_number(self):
        """Test case for an even number."""
        self.assertEqual(4 % 2, 0)  # Example: 4 is even

    def test_check_number_negative_even_number(self):
        """Test case for a negative even number."""
        self.assertEqual(-6 % 2, 0)  # Example: -6 is even

    def test_check_number_negative_odd_number(self):
        """Test case for a negative odd number."""
        self.assertEqual(-7 % 2, 1)  # Example: -7 is odd (Python's modulus keeps sign)

    def test_check_number_neutral(self):
        """Test case for zero (neutral number)."""
        self.assertEqual(0 % 2, 0)  # Zero is considered even

    def test_check_number_odd_number(self):
        """Test case for an odd number."""
        number = 3
        self.assertEqual(number % 2, 1)  # Odd numbers have remainder 1 when divided by 2

    def test_check_number_even_number(self):
        """Test case for an even number."""
        number = 4
        self.assertEqual(number % 2, 0)  # Even numbers have remainder 0 when divided by 2

    def test_check_number_negative_even_number(self):
        """Test case for a negative even number."""
        number = -6
        self.assertEqual(number % 2, 0)  # Negative even numbers still have remainder 0

    def test_check_number_negative_odd_number(self):
        """Test case for a negative odd number."""
        number = -7
        self.assertEqual(number % 2, 1)  # Odd numbers (even if negative) have remainder 1

    def test_check_number_neutral(self):
        """Test case for zero (neutral number)."""
        number = 0
        self.assertEqual(number % 2, 0)  # Zero is considered even
