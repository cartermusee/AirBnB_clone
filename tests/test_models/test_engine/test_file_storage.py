#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import re
import json
import uuid
import os
import time
"""class for test filestoarage"""


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.save()

    def tearDown(self):
        try:
            os.remove(FileStorage.__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """test for all method"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 2)

    def test_new(self):
        """test for the new method"""
        obj3 = BaseModel()
        self.storage.new(obj3)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 3)

    def test_save_and_reload(self):
        """Save data to file
        then clear objects
        reload from file, and compare"""
        self.storage.save()
        FileStorage.__objects = {}
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIsInstance(all_objects.get("BaseModel.{}".format(self.obj1.id)), BaseModel)
        self.assertIsInstance(all_objects.get("BaseModel.{}".format(self.obj2.id)), BaseModel)

if __name__ == '__main__':
    unittest.main()

