#!/usr/bin/python3

import unittest
import pycodestyle
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def test_subclass(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
        self.assertTrue(city, "state_id")
        self.assertIs(type(city.state_id), str)
        self.assertEqual(city.state_id, "")
        self.assertTrue(city, "name")
        self.assertIs(type(city.name), str)
        self.assertEqual(city.name, "")
        
    def test_pep8(self):
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/city.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")


    if __name__ == '__main__':
        unittest.main()
