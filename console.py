#!/usr/bin/python3
"""This is a class"""
import cmd
from models.base_model import *
import sys
from models import storage
class HBNBCommand(cmd.Cmd):
    classes = {
        "BaseModel"
    }
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, input):
        args = input.split()
        
        if not input:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print(f"** class {args[0]} doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Muestra la representación en cadena de una instancia."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.storage.objectClass:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in self.storage.all():
            instance = self.storage.all()[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] in self.cls:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = args[0] + '.' + args[1]
                    objects = storage.all()
                    if key in objects:
                        del objects[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
