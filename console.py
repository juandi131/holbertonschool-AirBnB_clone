#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    intro = "Welcome to the console"
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
