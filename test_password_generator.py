import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_lowercase_only(self):
        pwd = generate_password(8, False, False, False)
        self.assertEqual(len(pwd), 8)
        self.assertTrue(pwd.islower())

    def test_includes_uppercase(self):
        pwd = generate_password(10, True, False, False)
        self.assertEqual(len(pwd), 10)
        self.assertTrue(any(c.isupper() for c in pwd))

    def test_includes_numbers(self):
        pwd = generate_password(10, False, True, False)
        self.assertEqual(len(pwd), 10)
        self.assertTrue(any(c.isdigit() for c in pwd))

    def test_includes_special_chars(self):
        pwd = generate_password(10, False, False, True)
        self.assertEqual(len(pwd), 10)
        self.assertTrue(any(c in '!@#$%^&*()-_=+[{]};:\'",<.>/?`~' for c in pwd))

    def test_invalid_no_chars(self):
        with self.assertRaises(ValueError):
            generate_password(8, False, False, False)

if __name__ == '__main__':
    unittest.main()

