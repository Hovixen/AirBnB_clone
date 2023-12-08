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
        Creates a new instance of a specified class, saves it to the JASON file
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

if __name__ == '__main__':
    # try:
    HBNBCommand().cmdloop()
    # except KeyboardInterrupt:
    #    print('')
    #    exit
