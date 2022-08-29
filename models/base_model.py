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
        self.__class__ = self.__class__


    def __str__(self):
        return  BaseModel.__name__ + "(" + self.id + ")" + str(self.__dict__)

    def save(self):
        change = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        mydict = dict(self.__dict__)
        mydict["self.created_at"] = self.created_at.isoformat()
        mydict["self.updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] =  type(self).__name__
        return mydict