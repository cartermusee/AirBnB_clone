#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import datetime
"""module for basemodel test"""



class TestBaseModel(unittest.TestCase):
    """cases for basemodel"""

    def test_instances(self):
        """test for instances"""

        base = BaseModel
        self.assertFalse(issubclass(type(base), BaseModel))

    def test_3_id(self):
        """unique user id test."""

        ld = [BaseModel().id for _ in range(1000)]
        self.assertEqual(len(set(ld)), len(ld))

    def test_str(self):
        """test for string rep"""
        base = BaseModel()
        rep = str(base)
        self.assertTrue('[BaseModel]' in rep)
        self.assertTrue(base.id in rep)

    def test_save(self):
        """test for the save mrthod"""
        base = BaseModel()
        old_up = base.updated_at
        base.save()
        self.assertNotEqual(old_up, base.updated_at)
        curerent = datetime.datetime.now()
        time_dff = base.updated_at - curerent
        self.assertTrue(time_dff.total_seconds() < 1)

    def test_to_dict(self):
        """test for the method to_dict"""
        base = BaseModel()
        base_d = base.to_dict()
        answer = {
            'id': base.id,
            'created_at': base.created_at.isoformat(),
            'updated_at': base.updated_at.isoformat(),
            '__class__': "BaseModel"
        }
        self.assertEqual(base_d, answer)

        base_instance = base.to_dict()
        self.assertIsInstance(base_instance, dict)
        self.assertTrue('id' in base_instance)
        self.assertTrue('created_at' in base_instance)
        self.assertTrue('updated_at' in base_instance)
        self.assertTrue('__class__' in base_instance)

        """to test for the datetime if they are good"""
        base_created_at = datetime.datetime.strptime(base_instance['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        base_updated_at = datetime.datetime.strptime(base_instance['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(base_created_at, base.created_at)
        self.assertEqual(base_updated_at, base.updated_at)

    def test_invalid(self):
        """test inavalid"""
        with self.assertRaises(ValueError):
            BaseModel(created_at = "wrong_date")
        with self.assertRaises(ValueError):
            BaseModel(updated_at = "wrong_date")

    def test_call_save_many(self):
        """calling save multiple"""
        base = BaseModel()
        up = base.updated_at
        base.save()
        base.save()
        self.assertNotEqual(up, base.updated_at)
        self.assertEqual(base.updated_at, base.updated_at)

    def test_cust(self):
        """test for custom values"""
        base = BaseModel()
        base.name = "carter musee"
        base_d = base.to_dict()
        answer = {
            'id': base.id,
            'created_at': base.created_at.isoformat(),
            'updated_at': base.updated_at.isoformat(),
            '__class__': "BaseModel",
            'name': "carter musee"
        }
        self.assertEqual(base_d, answer)
        base_instance = base.to_dict()
        self.assertIsInstance(base_instance, dict)
        self.assertTrue('id' in base_instance)
        self.assertTrue('created_at' in base_instance)
        self.assertTrue('updated_at' in base_instance)
        self.assertTrue('__class__' in base_instance)
        self.assertTrue('name' in base_instance)

    def test_time_str(self):
        """test time if string passed"""
        dt_str = "2023-08-09t12:34:56.79999"
        dt_obj = datetime.datetime.strptime(
                dt_str, "%Y-%m-%dT%H:%M:%S.%f")
        base = BaseModel()
        base.created_at = dt_obj
        base.updated_at = dt_obj
        base_dt = base.to_dict()
        answer = {
            'id': base.id,
            'created_at': dt_obj.isoformat(),
            'updated_at': dt_obj.isoformat(),
            '__class__': "BaseModel"
        }
        self.assertEqual(base_dt, answer)


if __name__ == '__main__':
    unittest.main()
