#!/usr/bin/python3
from models.base_model import BaseModel
"""Creating new classes"""


class Review(BaseModel):
    """Creating a new class Review"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
