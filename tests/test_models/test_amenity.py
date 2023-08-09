#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""class for amenity test"""


class TestAmenity(unittest.TestCase):
    """test for amenity"""
    def test_inheritance(self):
        """test inheritance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_instances(self):
        """test for instances"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_name(self):
        """test if name is good"""
        am = Amenity()
        am.name = "musee"
        self.assertEqual(am.name, "musee")

    def test_to_dict_on_name(self):
        """test the input of amenity if it is converted to dict"""
        am = Amenity()
        am.name = "musee"
        am_dict = am.to_dict()
        self.assertIsInstance(am_dict, dict)
        self.assertEqual(am_dict['name'], 'musee')


if __name__ == "__main__":
    unittest.main()
