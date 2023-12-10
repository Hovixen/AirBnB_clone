#!/usr/bin/python3
"""Test module"""


import unittest
from models.city import City


class TestMyCity(unittest.TestCase):
    """New class to test class City"""

    def setUp(self):
        """Setting up"""
        self.new = City()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if new instance belongs to class City"""
        self.assertTrue(type(self.new) is City)

    def test_id(self):
        """Check if state_id is a string"""
        self.assertTrue(type(self.new.state_id) is str)

    def test_name(self):
        """Check if name is a str"""
        self.assertTrue(type(self.new.name) is str)

if __name__ == '__main__':
    unittest.main()
