#!/usr/bin/python3
""" This console is for manipulating objects with certain comands """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The class responsible for the commands to manipulate the objects """
    prompt = "(hbnb) "

    list_cls = [BaseModel, User, Amenity, City, Place, State, Review]
    class_dic = {classes.__name__: classes for classes in list_cls}

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ End of file function with Ctrl D """
        print("")
        return True

    def emptyline(self):
        """ does not execute anything for an empty line """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a specified class, saves it to the JSON file
        and prints its ID
        Syntax: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in [cls.__name__ for cls in HBNBCommand.list_cls]:
            print("** class doesn't exist **")
        else:
            instance_model = HBNBCommand.class_dic[arg]()
            instance_model.save()
            print(instance_model.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and ID
        Syntax: show <class_name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        arg = args.split()
        cls_name = arg[0]

        if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            cls_id = arg[1].strip('"')
            get_objects = storage.all()
            for key, obj in get_objects.items():
                name_obj = obj.__class__.__name__
                id_obj = obj.id
                if name_obj == cls_name and id_obj == cls_id:
                    print(obj)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and ID
        (Save the change into the JSON file)
        Syntax: destroy <class_name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        arg = args.split()
        cls_name = arg[0]

        if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            cls_id = arg[1].strip('"')
            get_objects = storage.all()
            delete_key = []

            for key, obj in get_objects.items():
                name_obj = obj.__class__.__name__
                id_obj = obj.id
                if name_obj == cls_name and id_obj == cls_id:
                    delete_key.append(key)

            if delete_key:
                for key in delete_key:
                    del storage._FileStorage__objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instance
        based or not on the class name
        Syntax: all or all <class_name>
        """
        arg = args.split()
        objects = []

        if not args:
            for obj in storage.all().values():
                objects.append(str(obj))
            print(objects)
        else:
            cls_name = arg[0]
            if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
                print("** class doesn't exist **")
            else:
                for key, obj in storage.all().items():
                    if cls_name == key.split('.')[0]:
                        objects.append(str(obj))
                print(objects)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute.
        Syntax: update <class_name> <id> <attribute_name> "<attribute_val>" or
                <class name>.update(<id>, <dictionary representation>) or
                <class_name>.update(<id>, <attribute_name>, <attribute_val>)
        """

        if not args:
            print("** class name missing **")
            return

        arg = args.split()
        cls_name = arg[0]

        if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            cls_id = arg[1]
            obj_key = cls_name + "." + cls_id

            if obj_key not in storage.all():
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                attr_name = arg[2]
                attr_val = arg[3].strip('"')

                objects = storage.all()[obj_key]
                setattr(objects, attr_name, attr_val)
                objects.save()

    def do_count(self, args):
        """
        Retrieves the number of instance of a class
        Syntax: <class_name>.count()
        """
        if not args:
            print("** class name missing **")
        else:
            cls_name = args.split('.')[0]
            if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
                print("** class doesn't exist **")
            else:
                count = 0
                for obj in storage.all().values():
                    if isinstance(obj, HBNBCommand.class_dic[cls_name]):
                        count += 1
                print(count)

    def custom_cmd(self, args):
        """
        Executes a custom command
        Syntax: <class_name>.<command>(<args>)
        Example: User.show("95b89993-f866-4f93-b4c0-990389b518b1")
        """
        cmd_list = ["create", "count", "all", "show", "destroy", "update"]
        if not args:
            print("** command missing **")
        else:
            arg_split = args.split('.')

            if len(arg_split) == 2:
                # prevents UnboundLocalError
                command = None
                try:
                    # assign class name and command with arguments
                    cls_name, cmd_with_arg = arg_split

                    # assign command and arguments
                    command, arg = cmd_with_arg[:-1].split('(')

                    if command not in cmd_list:
                        print("*** Unknown syntax: {}".format(args))
                except ValueError:
                    print("*** Unknown syntax: {}".format(args))
            else:
                print("*** Unknown syntax: {}".format(args))
                return

            if command == "create":
                self.do_create(cls_name)
            elif command == "count":
                self.do_count(cls_name)
            elif command == "all":
                self.do_all(cls_name)
            elif command == "show":
                self.do_show('{} {}'.format(cls_name, arg))
            elif command == "destroy":
                self.do_destroy('{} {}'.format(cls_name, arg))
            elif command == "update":
                self.do_update('{} {}'.format(cls_name, arg))

    def default(self, line):
        """
        Default method to handle customized commands
        """
        self.custom_cmd(line)


if __name__ == '__main__':
    # try:
    HBNBCommand().cmdloop()
    # except KeyboardInterrupt:
    # print('')
    # exit
