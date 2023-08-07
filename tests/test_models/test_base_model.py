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


class TestBaseModel(unittest.TestCase):
    """cases for basemodel"""

    def test_instances(self):
        """test for instances"""

        base = BaseModel
        self.assertAlmostEqual(str(type(base)), "<class models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(base), BaseModel))
        self.assertIsInstance(base, BaseModel)
