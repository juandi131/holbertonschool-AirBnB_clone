#!/usr/bin/python3
import json
"""Writing a class FileStorage that serializes 
nstances to a JSON file and deserializes JSON
file to instances:"""


class FileStorage():
    """creating the class FileStorage"""
    def __init__(self):
        """Initializing the class"""
        self.__file_path = "file.json"
        self.__objects = {}
        
    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        variable = {key: value for key,value in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(variable, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists;otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                cont = json.load(file)
                for key, value in cont.items():
                    obj = self.objclass[value['__class__']](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
