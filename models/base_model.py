#!/usr/bin/python3
import uuid
from datetime import datetime
"""Creating a base model that defines common attributes"""


class BaseModel:
    """defining the class"""
    def __init__(self, otherId=None):
        """defining the init of the class Base Model"""
        if otherId is not None:
            self.id = otherId
        else:
            self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Defining save public instance method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Defining to dict public instance method"""
        instanceDict = self.__dict__.copy()
        instanceDict['__class__'] = self.__class__.__name__
        instanceDict['updated_at'] = self.updated_at.isoformat()
        instanceDict['created_at'] = self.created_at.isoformat()
        return instanceDict

    def __str__(self):
        """Defining __str__"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
