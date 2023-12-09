#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        instance = BaseModel()
        result_dict = instance.to_dict()

        """Check if keys are present in the dictionary"""
        self.assertIn('id', result_dict)
        self.assertIn('created_at', result_dict)
        self.assertIn('updated_at', result_dict)
        self.assertIn('__class__', result_dict)

        """Check if values are of the expected types"""
        self.assertIsInstance(result_dict['id'], str)
        self.assertIsInstance(result_dict['created_at'], str)
        self.assertIsInstance(result_dict['updated_at'], str)
        self.assertIsInstance(result_dict['__class__'], str)

        """Check if datetime strings can be
        converted back to datetime objects"""
        created_at = datetime.strptime(
                result_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(
                result_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        """Check if datetime objects are approximately equal"""
        self.assertAlmostEqual(
                instance.created_at.timestamp(),
                created_at.timestamp(), places=2)
        self.assertAlmostEqual(
                instance.updated_at.timestamp(),
                updated_at.timestamp(), places=2)

    def test_init_with_kwargs(self):
        kwargs_data = {
            "id": "some_id",
            "created_at": "2023-12-06T12:00:00.000000",
            "updated_at": "2023-12-06T14:30:00.000000",
            "custom_attribute": "custom_value"
        }

        instance = BaseModel(**kwargs_data)

        """Check if attributes are set correctly"""
        self.assertEqual(instance.id, kwargs_data['id'])
        self.assertEqual(
                instance.created_at.isoformat(), kwargs_data['created_at'])
        self.assertEqual(
                instance.updated_at.isoformat(), kwargs_data['updated_at'])

        """Check if the custom attribute is set correctly"""
        self.assertEqual(getattr(
            instance, 'custom_attribute', None),
            kwargs_data['custom_attribute'])


if __name__ == '__main__':
    unittest.main()
