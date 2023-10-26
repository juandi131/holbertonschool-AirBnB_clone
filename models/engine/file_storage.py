#!/usr/bin/python3
import json
import os


class FileStorage():
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
        
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    def save(self):
        variable = {key: value for key,value in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(variable, file)
