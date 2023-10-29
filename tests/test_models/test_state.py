#!/usr/bin/python3

import unittest
import pycodestyle
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):


    def test_pep8(self):
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/state.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
        self.assertTrue(state, "name")
        self.assertIs(type(state.name), str)
        self.assertEqual(state.name, "")
        
    def test_attributes(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
        self.assertTrue(state, "name")
        self.assertIs(type(state.name), str)
        self.assertEqual(state.name, "")

    if __name__ == '__main__':
        unittest.main()
