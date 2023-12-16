#!/usr/bin/python3
"""Defines unittests for models/user.py"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class"""

    def setUp(self):
        """Set up User instance for tests"""
        self.instance = User()

    def test_init_attributes(self):
        """Check correct init attribute values"""

        email = self.instance.email
        password = self.instance.password
        first_name = self.instance.first_name
        last_name = self.instance.last_name

        self.assertEqual(email, "")
        self.assertEqual(password, "")
        self.assertEqual(first_name, "")
        self.assertEqual(last_name, "")

    def test_set_attributes(self):
        """Check for correct attribute values once set"""

        self.instance.email = "dornkaizen@gmail.com"
        self.instance.password = "123"
        self.instance.first_name = "Demi"
        self.instance.last_name = "Nelson"

        self.assertEqual(self.instance.email, "demikaizen@gmail.com")
        self.assertEqual(self.instance.password, "123")
        self.assertEqual(self.instance.first_name, "Demi")
        self.assertEqual(self.instance.last_name, "Nelson")


if __name__ == "__main__":
    unittest.main()
