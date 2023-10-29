#!/usr/bin/python3

import unittest
import pycodestyle
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_pep8(self):
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/amenity.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))
        self.assertTrue(amenity, "name")
        self.assertIs(type(amenity.name), str)
        self.assertEqual(amenity.name, "")

    def test_subclass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))


    if __name__ == '__main__':
        unittest.main()
    