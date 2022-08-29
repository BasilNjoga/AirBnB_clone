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
        return  f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        change = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """ Returns dictionary representation of all key/vlaues of dict"""
        mydict = dict(self.__dict__)
        mydict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        mydict["self.updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        mydict["__class__"] =  type(self).__name__
        return mydict