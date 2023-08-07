#!/usr/bin/python3

import os
import json
"""class filestorage"""


class FileStorage:

    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = "{},{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding='utf-8') as fl:
            data = {}
            for key, value in FileStorage.__objects.items():
                data[key] = value.to_dict()

            json.dumps(data, fl)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            FileStorage.__objects = obj_dict
