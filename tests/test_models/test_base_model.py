import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        # Test id attribute
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)

        # Test created_at and updated_at attributes
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_method(self):
        # Test __str__ method
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Check updated_at value after save is executed"""
        current_value = self.instance.updated_at
        new_value = self.instance.save()

        self.assertNotEqual(current_value, new_value)

    def test_to_dict_method(self):
        # Test to_dict method
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

        # Check that created_at and updated_at are in ISO format strings
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_unique_ids(self):
        # Test unique ids for different instances
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_uuid_format(self):
        # Test that id is a valid UUID
        obj = BaseModel()
        try:
            uuid.UUID(obj.id, version=4)
        except ValueError:
            self.fail("Invalid UUID format for id")


if __name__ == '__main__':
    unittest.main()
