#!/usr/bin/python3
"""this module contains a class filestorage"""
import json
import os


class FileStorage:
    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes BaseModel object(__objects)
            to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fl:
            data = {}
            for key, value in FileStorage.__objects.items():
                data[key] = value.to_dict()
            json.dump(data, fl)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.user import User
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            loaded_objects = {}
            for k, v in obj_dict.items():
                if 'User' in v.keys():
                    loaded_objects[k] = User(**v)
                elif 'Amenity' in v.keys():
                    loaded_objects[k] = Amenity(**v)
                elif 'City' in v.keys():
                    loaded_objects[k] = City(**v)
                elif 'Place' in v.keys():
                    loaded_objects[k] = Place(**v)
                elif 'Review' in v.keys():
                    loaded_objects[k] = Review(**v)
                elif 'State' in v.keys():
                    loaded_objects[k] = State(**v)
                else:
                    loaded_objects[k] = BaseModel(**v)
            FileStorage.__objects = loaded_objects
