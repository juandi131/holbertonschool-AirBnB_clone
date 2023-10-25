#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    intro = "Bienvenido a la consola"
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        return True
    def do_create(self, arg):
        """
        Create a new object.
        
        Usage: create <class_name>
        Example: create User
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
