#!/usr/bin/python3
"""Test module"""


import unittest
from models.amenity import Amenity


class TestMyAmenity(unittest.TestCase):
    """New class to test class Amenity"""

    def setUp(self):
        """Setting up"""
        self.new = Amenity()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.new, Amenity)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertIsInstance(self.new.name, str)

if __name__ == '__main__':
    unittest.main()
