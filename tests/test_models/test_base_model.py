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
        self.assertAlmostEqual(
                str(type(base)), "<class models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(base), BaseModel))
        self.assertIsInstance(base, BaseModel)

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
        self.assertEqual(time_dff.total_seconds() < 1)

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
        base_created_at = datetime.strptime(
                base_instance['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        base_updated_at = datetime.strptime(
                base_instance['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(base_created_at, base.created_at)
        self.assertEqual(base_updated_at, base.updated_at)


if __name__ == '__main__':
    unittest.main()
