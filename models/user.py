#!/usr/bin/python3
from models.base_model import BaseModel
"""Creating new classes"""


class User(BaseModel):
    """"Creating class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
