# tests for the odd_or_even() function
import unittest

def odd_or_even(param):
    return param % 2 == 0
class TestOddOrEven(unittest.TestCase):

    def test_when_output_true(self):
        # write your tests here
        self.assertEqual(odd_or_even(2), True)

    def test_when_output_false(self):
        # write your tests here
        self.assertEqual(odd_or_even(1), False)



if __name__ == '__main__':
    unittest.main()