#!/usr/bin/python3
'''
This is a file for all my models
'''
import uuid
class BaseModel:
    """ defines all commond attributes and methods """
    def __init__(self,id,created_at, updated_at):
        self.id = str(uuid.uuid4())


    def __str__(self):
        return "[BaseModel] (" + self.id + ")" + self.dict
