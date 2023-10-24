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
<<<<<<< HEAD

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
# Crear una instancia de la clase BaseModel
lol = BaseModel()

# Llamar al método to_dict en la instancia
diccionario = lol.to_dict()

# Imprimir el diccionario
print(diccionario)
=======

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
>>>>>>> a4ae72f2e0bf5e02613ac9aeb8dd777e8752f67a
