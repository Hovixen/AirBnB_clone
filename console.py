#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
""" This console is for manipulating objects with certain comands """


class HBNBCommand(cmd.Cmd):
    """ The class responsible for the commands to manipulate the objects """
    prompt = "(hbnb) "

    list_cls = [BaseModel]
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

        arg = args.split(' ')
        cls_name = arg[0]

        if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id is missing **")
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

        arg = args.split(' ')
        cls_name = arg[0]
    
        if cls_name not in [cls.__name__ for cls in HBNBCommand.list_cls]:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id is missing **")
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


if __name__ == '__main__':
    # try:
    HBNBCommand().cmdloop()
    # except KeyboardInterrupt:
    #    print('')
    #    exit
