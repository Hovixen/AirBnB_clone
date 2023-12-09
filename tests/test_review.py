#!/usr/bin/python3
"""Test module"""


import unittest
from models.review import Review


class TestMyReview(unittest.TestCase):
    """New class to test class Review"""

    def setUp(self):
        """Setting up"""
        self.new = Review()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.new, Review)

    def test_if_str(self):
        """Check if the attrs are str"""
        self.assertIsInstance(self.new.place_id, str)
        self.assertIsInstance(self.new.user_id, str)
        self.assertIsInstance(self.new.text, str)

if __name__ == '__main__':
    unittest.main()
