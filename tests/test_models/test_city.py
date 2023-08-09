#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
"""test city"""


class Testcity(unittest.TestCase):
    """test"""
    def test_basemodel_inheritance(self):
        """test for basemodel inheritance"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_state_id(self):
        """test for state_id attribute"""
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_name(self):
        """test for name attribute"""
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_to_dict(self):
        """test for to_dict method"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        dict_city = city.to_dict()
        self.assertIsInstance(dict_city, dict)
        self.assertEqual(dict_city["state_id"], "CA")
        self.assertEqual(dict_city["name"], "San Francisco")


if __name__ == '__main__':
    unittest.main()
