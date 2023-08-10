#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place
"""test for place"""


class TestPlace(unittest.TestCase):
    """test for place"""
    def test_inheritance(self):
        """test for inheritance"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_city_id(self):
        """test for city_id"""
        place = Place()
        place.city_id = "1"
        self.assertEqual(place.city_id, "1")

    def test_user_id(self):
        """test for user_id """
        place = Place()
        place.user_id = "233"
        self.assertEqual(place.user_id, "233")

    def test_name(self):
        """test for name"""
        place = Place()
        place.name = "kwetu"
        self.assertEqual(place.name, "kwetu")

    def test_description(self):
        """test for description"""
        place = Place()
        place.description = "nice place"
        self.assertEqual(place.description, "nice place")

    def test_number_rooms(self):
        """test for number_rooms"""
        place = Place()
        place.number_rooms = 4
        self.assertEqual(place.number_rooms, 4)

    def test_number_bathrooms(self):
        """test for number_bathrooms"""
        place = Place()
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        """test for max_guest attribute"""
        place = Place()
        place.max_guest = 4
        self.assertEqual(place.max_guest, 4)

    def test_price_by_night(self):
        """test for price_by_night"""
        place = Place()
        place.price_by_night = 123
        self.assertEqual(place.price_by_night, 123)

    def test_latitude(self):
        """test for latitude"""
        place = Place()
        place.latitude = 32.45
        self.assertEqual(place.latitude, 32.45)

    def test_longitude(self):
        """test for longitude"""
        place = Place()
        place.longitude = -122.42
        self.assertEqual(place.longitude, -122.42)

    def test_amenity_ids(self):
        """test for amenity_ids"""
        place = Place()
        place.amenity_ids = []
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict(self):
        """test for to_dict method"""
        place = Place()
        place.city_id = "1"
        place.user_id = "2"
        place.name = "kwetu"
        place.description = "nice place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 123
        place.latitude = 123.45
        place.longitude = -122.42
        place.amenity_ids = ["1", "2"]
        dict_place = place.to_dict()
        self.assertIsInstance(dict_place, dict)
        self.assertEqual(dict_place["city_id"], "1")
        self.assertEqual(dict_place["user_id"], "2")
        self.assertEqual(dict_place["name"], "kwetu")
        self.assertEqual(dict_place["description"], "nice place")
        self.assertEqual(dict_place["number_rooms"], 2)
        self.assertEqual(dict_place["number_bathrooms"], 1)
        self.assertEqual(dict_place["max_guest"], 4)
        self.assertEqual(dict_place["price_by_night"], 123)
        self.assertEqual(dict_place["latitude"], 123.45)
        self.assertEqual(dict_place["longitude"], -122.42)
        self.assertEqual(dict_place["amenity_ids"], ['1', '2'])


if __name__ == "__main__":
    unittest.main()
