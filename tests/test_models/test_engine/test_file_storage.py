#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
"""class for filestorage"""


class TestFileStorage(unittest.TestCase):
    """tests"""

    def setUp(self):
        """setup"""
        self.storage = FileStorage()

    def tearDown(self):
        """teardown"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_new_and_all(self):
        """new and all methods"""
        model = BaseModel()
        self.storage.new(model)
        all_objects = self.storage.all()
        self.assertIn(model, all_objects.values())


if __name__ == '__main__':
    unittest.main()
