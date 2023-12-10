#!/usr/bin/python3
"""Test module"""


import unittest
from models.place import Place


class TestMyPlace(unittest.TestCase):
    """New class to test class Place"""

    def setUp(self):
        """Setting up"""
        self.new = Place()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if attributes are of a correct type"""
        self.assertIsInstance(self.new, Place)
        self.assertIsInstance(self.new.city_id, str)
        self.assertIsInstance(self.new.user_id, str)
        self.assertIsInstance(self.new.name, str)
        self.assertIsInstance(self.new.description, str)
        self.assertIsInstance(self.new.number_rooms, int)
        self.assertIsInstance(self.new.number_bathrooms, int)
        self.assertIsInstance(self.new.max_guest, int)
        self.assertIsInstance(self.new.price_by_night, int)
        self.assertIsInstance(self.new.latitude, float)
        self.assertIsInstance(self.new.city_id, str)
        self.assertIsInstance(self.new.longitude, float)
        self.assertIsInstance(self.new.amenity_ids, list)

    def test_if_attrs_exist(self):
        """Check if attributes are present in the class"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    if __name__ == '__main__':
        unittest.main()
