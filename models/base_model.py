#!/usr/bin/python3
""" This module contains a class BaseModel """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Initializes a class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Init method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if value is not None:
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, datetime.strptime(value, format))
                    else:
                        setattr(self, key, None)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict containing all key/value pairs of the dict
        representation of the instance, including the class name of the object
        created_at and updated_at are returned in isoformat(readable format)
        """
        dict_obj = self.__dict__.copy()
        dict_obj["created_at"] = dict_obj["created_at"].isoformat()
        dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()
        dict_obj["__class__"] = __class__.__name__
        return dict_obj
