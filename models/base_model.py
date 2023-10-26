#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""Creating a base model that defines common attributes"""


class BaseModel:
    """defining the class"""
    def __init__(self, *args, **kwargs):
        """defining the  init of the class Base Model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Defining save public instance method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Defining to dict public instance method"""
        instanceDict = self.__dict__.copy()
        instanceDict['__class__'] = type(self).__name__
        instanceDict['updated_at'] = self.updated_at.isoformat()
        instanceDict['created_at'] = self.created_at.isoformat()
        
        return instanceDict

    def __str__(self):
        """Defining __str__"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    