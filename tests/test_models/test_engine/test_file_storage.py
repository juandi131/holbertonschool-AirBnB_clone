#!/usr/bin/python3
""" Unittest for Test File storage. """
import json
import os
import unittest
import models
from unittest.mock import patch
from models.base_model import BaseModel
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.modeluno = BaseModel()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_adds_instance_to_objects(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.assertIn(key, self.storage.all())

    def test_models_storage(self):
        self.assertIsNotNone(models.storage.all())
        self.assertIsNone(models.storage.reload())

    def test_save_reload(self):
        self.storage.new(self.modeluno)
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        obj_key = "BaseModel." + self.modeluno.id
        obj_all = self.storage.all()
        obj_storage = obj_all[obj_key]
        self.assertIn(obj_key, self.storage.all())
        self.assertTrue(self.modeluno.__dict__ == obj_storage.__dict__)
        self.assertFalse(self.modeluno is obj_storage)
        self.assertIsInstance(obj_storage, BaseModel)
        self.assertEqual(self.modeluno.id, obj_storage.id)

def test_save_writes_to_file(self):
    obj = BaseModel()
    key = "{}.{}".format(type(obj).__name__, obj.id)
    self.storage.new(obj)

    temp_file = os.path.join(os.path.dirname(__file__), "temp_file.json")
    self.storage._FileStorage__file_path = temp_file

    self.storage.save()

    with open(temp_file, "r") as file:
        data = json.load(file)
        self.assertIn(key, data)
   
def test_reload_method(self):
    self.assertIsNotNone(FileStorage().reload)

def test_save_writes_to_file(self):
    obj = BaseModel()
    key = "{}.{}".format(type(obj).__name__, obj.id)
    self.storage.new(obj)

    temp_file = "temp_file.json"
    self.storage._FileStorage__file_path = temp_file

    self.storage.save()

    with open(temp_file, "r") as file:
        data = json.load(file)
        self.assertIn(key, data)

    def test_all_subclass(self):
        cls = {'BaseModel.': BaseModel, 'User.': User, 'State.': State,
               'City.': City, 'Amenity.': Amenity, 'Place.': Place,
               'Review.': Review}
        dic = {}
        stor_all = self.storage.all()
        for k, v in cls.items():
            dic[k] = v()
        for k, v in dic.items():
            self.assertIsNotNone(stor_all[k + v.id])      
   
if __name__ == "__main__":
    unittest.main()
