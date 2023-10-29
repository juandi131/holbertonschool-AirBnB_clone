#!/usr/bin/python3
""" The console """
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Definition of the hbnb console. """

    prompt = "(hbnb) "
    clas = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }

    def do_EOF(self, line):
        """Quit console at EOF."""
        print("")
        return True

    def do_quit(self, line):
        """Quit the console."""
        return True

    
    def emptyline(self):
        pass
<<<<<<< HEAD
    
    def do_create(self, arg):
        obj = BaseModel()
        obj.save()
        print(obj.id)
        
=======

    def do_create(self, line):
        """Crea una nueva instancia"""
        try:
            list = line.split(" ")
            objeto = eval(list[0])()
            objeto.save()
            print(objeto.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """imprime la representacione de una instancia."""
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.clas:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """destruye una instanci"""
        try:
            if not line:
                raise SyntaxError()
            lista = line.split(" ")
            if lista[0] not in self.clas:
                raise NameError()
            if len(lista) < 2:
                raise IndexError()
            objects = storage.all()
            key = lista[0] + '.' + lista[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """imprime todo"""
        objects = storage.all()
        lista = []
        if not line:
            for key in objects:
                lista.append(str(objects[key]))
            print(lista)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.clas:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    lista.append(str(objects[key]))
            print(lista)
        except NameError:
            print("** class doesn't exist **")

>>>>>>> 0a4ce58aa89ab9f080faed100edccfb8e7abfee3

if __name__ == '__main__':
    HBNBCommand().cmdloop()