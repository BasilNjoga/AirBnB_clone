#!/usr/bin/python3
'''
This is a file for all my models
'''
import uuid
from datetime import datetime
from datetime import date


class BaseModel:
    """ defines all commond attributes and methods """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns dictionary representation of all key/vlaues of dict"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        mydict = dict(self.__dict__)
        mydict["__class__"] = type(self).__name__
        return mydict
