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
        "Amenity",
        "City",
        "State",
        "Place",
        "Review",
        "User"
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
            lista = line.split(" ")
            if len(lista) < 2:
                raise IndexError()
            if lista[0] not in self.clas:
                raise NameError()
            objetos = storage.all()
            key = lista[0] + '.' + lista[1]
            if key in objetos:
                print(objetos[key])
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
            if len(lista) < 2:
                raise IndexError()
            if lista[0] not in self.clas:
                raise NameError()
            objectos = storage.all()
            key = lista[0] + '.' + lista[1]
            if key in objectos:
                del objectos[key]
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

    def do_update(self, line):
        """Updates"""
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
            if key not in objects:
                raise KeyError()
            if len(lista) < 3:
                raise AttributeError()
            if len(lista) < 4:
                raise ValueError()
            for k, v in objects.items():
                if k == key:
                    v.__dict__[lista[2]] = eval(lista[3])
                    v.save()
                    return

        except IndexError:
            print("** instance id missing **")
        except AttributeError:
            print("** attribute name missing **")
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except ValueError:
            print("** value missing **")
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
