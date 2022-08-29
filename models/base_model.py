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
        return  BaseModel.__name__ + "(" + self.id + ")" + str(self.__dict__)

    def save(self):
        change = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__class__
        return self.__dict__