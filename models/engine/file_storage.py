#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

"""Writing a class FileStorage that serializes 
nstances to a JSON file and deserializes JSON
file to instances:"""


class FileStorage():
    """creating the class FileStorage"""
    __file_path = "file.json"
    __objects = {}
    objectClass = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                   "City": City, "Place": Place, "Review": Review}
        
    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        try:
            variable = {}
            for key, value in self.__objects.items():
                variable[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(variable, file, indent=4)
        except Exception:
            pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists;otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                inside = json.load(file)
                for key, value in inside.items():
                    obj = self.objectClass[value["__class__"]](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
