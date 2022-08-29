#!/usr/bin/python3
'''
This is a file for all my models
'''
import uuid
from datetime import datetime
from datetime import date

class BaseModel:
    """ defines all commond attributes and methods """
    def __init__(self):
        self.id = str(uuid.uuid4())
        current = datetime.now()
        update = datetime.now()
        self.created_at = current.isoformat()
        self.updated_at = update.isoformat()



    def __str__(self):
        return "[BaseModel] (" + self.id + ")"

    def save(self):
        change = datetime.now()
        self.updated_at = change.isoformat()
    
    def to_dict(self):
        return dict()