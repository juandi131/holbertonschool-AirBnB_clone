#!/usr/bin/python3
from models.base_model import BaseModel
"""Creating new classes"""


class User(BaseModel):
    """"Creating class User that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Defining initialization of email, password, first and last name"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
