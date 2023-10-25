#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    intro = "Bienvenido a la consola"
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True
    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
