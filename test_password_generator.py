import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_lowercase_only(self):
        # Test only lowercase characters
        pwd = generate_password(8, True, False, False, False)  # Added use_special_chars
        self.assertEqual(len(pwd), 8)
        self.assertTrue(pwd.islower())

    def test_includes_uppercase(self):
        # Test includes uppercase letters
        pwd = generate_password(10, True, True, False, False)  # Added use_special_chars
        self.assertEqual(len(pwd), 10)
        self.assertTrue(any(c.isupper() for c in pwd))

    def test_includes_numbers(self):
        # Test includes numbers
        pwd = generate_password(10, False, False, True, False)  # Added use_special_chars
        self.assertEqual(len(pwd), 10)
        self.assertTrue(any(c.isdigit() for c in pwd))

    def test_includes_special_chars(self):
        # Test includes special characters
        pwd = generate_password(10, False, False, False, True)  # Added use_special_chars
        self.assertEqual(len(pwd), 10)
        self.assertTrue(any(c in '!@#$%^&*()-_=+[{]};:\'",<.>/?`~' for c in pwd))

    def test_invalid_no_chars(self):
        # Test invalid case with no character types selected
        with self.assertRaises(ValueError):
            generate_password(8, False, False, False, False)  # Added use_special_chars

if __name__ == '__main__':
    unittest.main()
