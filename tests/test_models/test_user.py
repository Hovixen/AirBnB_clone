#!/usr/bin/python3
"""New testing module"""
import unittest
from models.base_model import BaseModel
from models.user import User
import os


class TestMyUser(unittest.TestCase):
    """Class TestMyUser to test class User"""

    def setUp(self):
        """setting up each test"""
        self.new = User()
        self.base = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """cleaning up after each test"""
        del self.new
        del self.base
        del self.base2
        # os.remove("file.json")

    def test_empty_strings_before(self):
        """Check if the strings are empty before assignment"""
        self.assertFalse(self.new.email)
        self.assertFalse(self.new.password)
        self.assertFalse(self.new.first_name)
        self.assertFalse(self.new.last_name)

    def test_methods_exist(self):
        """Check if the methods are present"""
        assert self.new.__init__ is not None
        assert self.new.save is not None
        assert self.new.to_dict is not None
        assert self.new.updated_at is not None
        assert self.new.__str__ is not None

    def test_attributes_exist(self):
        """Assign attributes and check if they are not None"""
        self.new.email = \
            'holbertonschoolisthebestschoolever@this.world'
        self.new.password = 'imnottellingyoumypassword'
        self.new.first_name = 'Diva'
        self.new.last_name = 'Mapatelian'

        self.assertNotEqual(self.new.email, None)
        self.assertNotEqual(self.new.password, None)
        self.assertNotEqual(self.new.first_name, None)
        self.assertNotEqual(self.new.last_name, None)

    def test_attributes_are_correct(self):
        """Check if assigments happened as intended"""
        self.new.email = 'holbertonschoolisthebestschoolever@this.world'
        self.new.password = 'imnottellingyoumypassword'
        self.new.first_name = 'Diva'
        self.new.last_name = 'Mapatelian'

        self.assertEqual(self.new.email,
                         'holbertonschoolisthebestschoolever@this.world')
        self.assertEqual(self.new.password, 'imnottellingyoumypassword')
        self.assertEqual(self.new.first_name, 'Diva')
        self.assertEqual(self.new.last_name, 'Mapatelian')

    def test_if_str(self):
        """Check if the attributes are strings"""

        self.new.email = 'holbertonschoolisthebestschoolever@this.world'
        self.new.password = 'imnottellingyoumypassword'
        self.new.first_name = 'Diva'
        self.new.last_name = 'Mapatelian'

        self.assertTrue(type(self.new.email) is str)
        self.assertTrue(type(self.new.password) is str)
        self.assertTrue(type(self.new.first_name) is str)
        self.assertTrue(type(self.new.last_name) is str)

    def test_right_class(self):
        """Check if the instance belongs to a right class"""
        self.assertIs(type(self.base), BaseModel)
        self.assertIsInstance(self.new, User)

    # check if file.json exists before running
    # def test_json_exists(self):
    #     self.assertFalse(os.path.exists("file.json"))

    def test_save(self):
        """check if save() writes in an empty file"""
        self.new.save()
        self.assertFalse(os.stat("file.json").st_size == 0)

    def test_json_size_changed(self):
        """Check the size of file.json, invoke save()
        and check if the size have changed"""
        before = os.stat('file.json').st_size
        self.base.save()
        after = os.stat('file.json').st_size
        self.assertFalse(before == after)

    def test_too_many_str(self):
        """Pass too many/no parameters to __str__"""
        with self.assertRaises(TypeError) as omg:
            self.new.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_dict(self):
        """Pass too many/no parameters to to_dict()"""
        with self.assertRaises(TypeError) as omg:
            self.new.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)

    def test_too_many_save(self):
        """Pass too many/no parameters to save()"""
        with self.assertRaises(TypeError) as omg:
            self.new.save('omg', 'lol', 'dolls')
        self.assertTrue(omg)


if __name__ == '__main__':
    unittest.main()
