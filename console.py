#!/usr/bin/python3
"""This is a class"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D"""
        return True

    def emptyline(self):
        """sexo"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
