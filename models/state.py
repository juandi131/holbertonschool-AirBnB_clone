#!/usr/bin/python3
from models.base_model import BaseModel
"""Creating new classes"""


class State(BaseModel):
    """Creating Class State that inherits from Base Model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
