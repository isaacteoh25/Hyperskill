# tests for the string_to_lower() function
import unittest


class TestStringToLower(unittest.TestCase):
    def test_string_to_lower(self):
        # testing for an exception one way
        # s = 'hello world'
        # self.assertEqual(s.split(), ['hello', 'world'])
        # self.assertRaises(string_to_lower())
        self.assertTrue(string_to_lower('Foo'), ValueError)
        self.assertRaises(ValueError, string_to_lower, 1)

        # testing for an exception another way
        with self.assertRaises(ValueError):
            string_to_lower(1)

if __name__ == '__main__':
    unittest.main()