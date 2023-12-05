#!/usr/bin/python3

import cmd
""" This console is for manipulating objects with certain comands """


class HBNBCommand(cmd.Cmd):
    """ The class responsible for the commands to manipulate the objects """
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    # try:
    HBNBCommand().cmdloop()
    # except KeyboardInterrupt:
    #    print('')
    #    exit
