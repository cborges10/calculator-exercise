import unittest

class TestCalculator(unittest.TestCase):
    def test_multiplication(self):
        # Test multiplication of two numbers
        a = 3
        b = 4
        result = a * b
        self.assertEqual(result, 12)
        
if __name__ == '__main__':
    unittest.main()
