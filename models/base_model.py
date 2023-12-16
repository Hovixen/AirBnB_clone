#!/usr/bin/python3
""" class Basemodel """


import uuid
from datetime import datetime
from models import storage
import sys
#from models.engine.file_storage import storage


class BaseModel():
    """ creation of BaseModel class """
    def __init__(self, *args, **kwargs):
        """ initialization of Base class """
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if key != "__class__":
<<<<<<< HEAD
                    #if key in ["created_at", "updated_at"]:
                        #value = datetime.strptime(
                                #value, "%Y-%m-%dT%H:%M:%S.%f")
=======
                    if key in ["updated_at", "created_at"]:
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
>>>>>>> baa8c7fe3abb3841de737daf05672edc464469c4
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """ string representation """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ save method """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ method returns a dict with keys/values """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        #new_dict["created_at"] = self.created_at.isoformat()
        #new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
