#!/usr/bin/python3
"""This is a class"""
import cmd
from models.base_model import BaseModel


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
    
    def do_create(self, arg):
        obj = BaseModel()
        obj.save()
        print(obj.id)
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
