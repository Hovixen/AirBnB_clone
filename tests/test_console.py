#!/usr/bin/python3
"""
Unittest for the console.py testing for all the features
"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Redirect sys.stdout to StringIO for testing"""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore sys.stdout"""
        sys.stdout = sys.__stdout__

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

        # More Test Cases for do_create
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output_user = f.getvalue().strip()
            self.assertTrue(len(output_user) > 0)

            HBNBCommand().onecmd("create Amenity")
            output_amenity = f.getvalue().strip()
            self.assertTrue(len(output_amenity) > 0)

            # Invalid class name
            HBNBCommand().onecmd("create InvalidClass")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid, "** class doesn't exist **")

            # Missing class name
            HBNBCommand().onecmd("create")
            output_missing = f.getvalue().strip()
            self.assertEqual(output_missing, "** class name missing **")

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output_create = f.getvalue().strip()

            HBNBCommand().onecmd("show BaseModel {}".format(output_create))
            output_show = f.getvalue().strip()
            self.assertTrue("BaseModel" in output_show)
            self.assertTrue(output_create in output_show)

        # More Test Cases for do_show
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output_user = f.getvalue().strip()
            self.assertEqual(output_user, "** instance id is missing **")

            HBNBCommand().onecmd("show InvalidClass 123")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid, "** class doesn't exist **")

            HBNBCommand().onecmd("show BaseModel")
            output_missing = f.getvalue().strip()
            self.assertEqual(output_missing, "** instance id is missing **")

            HBNBCommand().onecmd("show BaseModel 123")
            output_not_found = f.getvalue().strip()
            self.assertEqual(output_not_found, "** no instance found **")

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output_create = f.getvalue().strip()

            HBNBCommand().onecmd("destroy BaseModel {}".format(output_create))
            HBNBCommand().onecmd("show BaseModel {}".format(output_create))
            output_show = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output_show)

        # More Test Cases for do_destroy
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            output_user = f.getvalue().strip()
            self.assertEqual(output_user, "** instance id is missing **")

            HBNBCommand().onecmd("destroy InvalidClass 123")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid, "** class doesn't exist **")

            HBNBCommand().onecmd("destroy BaseModel")
            output_missing = f.getvalue().strip()
            self.assertEqual(output_missing, "** instance id is missing **")

            HBNBCommand().onecmd("destroy BaseModel 123")
            output_not_found = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output_not_found)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)

        # More Test Cases for do_all
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output_user = f.getvalue().strip()
            self.assertTrue("User" not in output_user)

            HBNBCommand().onecmd("all InvalidClass")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid, "** class doesn't exist **")

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output_create = f.getvalue().strip()

            HBNBCommand().onecmd("update BaseModel {} name\
                                 'new_name'".format(output_create))
            HBNBCommand().onecmd("show BaseModel {}".format(output_create))
            output_show = f.getvalue().strip()
            self.assertTrue("new_name" in output_show)

        # More Test Cases for do_update
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            output_user = f.getvalue().strip()
            self.assertEqual(output_user, "** instance id missing **")

            HBNBCommand().onecmd("update InvalidClass 123")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid, "** class doesn't exist **")

            HBNBCommand().onecmd("update BaseModel")
            output_missing = f.getvalue().strip()
            self.assertEqual(output_missing, "** instance id missing **")

            HBNBCommand().onecmd("update BaseModel 123")
            output_not_found = f.getvalue().strip()
            self.assertEqual(output_not_found, "** no instance found **")

            HBNBCommand().onecmd("update BaseModel {}\
                                 name".format(output_create))
            output_attr_missing = f.getvalue().strip()
            self.assertEqual(output_attr_missing,
                             "** attribute name missing **")

            HBNBCommand().onecmd("update BaseModel {} name\
                                 'new_name' extra".format(output_create))
            output_val_missing = f.getvalue().strip()
            self.assertEqual(output_val_missing, "** value missing **")

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

        # More Test Cases for do_count
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            output_user = f.getvalue().strip()
            self.assertEqual(output_user, "0")

            HBNBCommand().onecmd("count InvalidClass")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid, "** class doesn't exist **")

            HBNBCommand().onecmd("count")
            output_missing = f.getvalue().strip()
            self.assertEqual(output_missing, "** class name missing **")

    def test_custom_cmd(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show('123')")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

        # More Test Cases for custom_cmd
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("InvalidClass.count()")
            output_invalid = f.getvalue().strip()
            self.assertEqual(output_invalid,
                             "*** Unknown syntax: InvalidClass.count()")

            HBNBCommand().onecmd("User.invalid_method()")
            output_method_invalid = f.getvalue().strip()
            self.assertEqual(output_method_invalid,
                             "*** Unknown syntax: User.invalid_method()")

            HBNBCommand().onecmd("BaseModel.show('123')")
            output_custom_show = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output_custom_show)

            HBNBCommand().onecmd("create BaseModel")
            output_create = f.getvalue().strip()

            HBNBCommand().onecmd("BaseModel.update('{}', \
                                 'name', 'new_name')".format(output_create))
            HBNBCommand().onecmd("show BaseModel {}".format(output_create))
            output_custom_update = f.getvalue().strip()
            self.assertTrue("new_name" in output_custom_update)


if __name__ == '__main__':
    unittest.main()
