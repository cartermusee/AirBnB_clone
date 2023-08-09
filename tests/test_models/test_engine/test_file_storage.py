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

    def test_save_and_reload(self):
        """save and reload methods"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage = FileStorage()  # Recreate storage to simulate a new instance
        self.storage.reload()
        loaded = self.storage.all()["BaseModel,"] + model.id
        self.assertEqual(model.id, loaded_model.id)
        self.assertEqual(model.created_at, loaded_model.created_at)
        self.assertEqual(model.updated_at, loaded_model.updated_at)

       

if __name__ == '__main__':
    unittest.main()

