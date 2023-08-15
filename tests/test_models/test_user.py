#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User

"""class for testing user"""


class TestReview(unittest.TestCase):
    """class to test"""

    def test_inheritance(self):
        """test inheritance"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_email(self):
        """test for email"""
        user = User()
        user.email = "mike@gmail.com"
        self.assertEqual(user.email, 'mike@gmail.com')

    def test_password(self):
        """to test user pass"""
        user = User()
        user.password = 'fd544'
        self.assertEqual(user.password, 'fd544')

    def test_user_firstname(self):
        """to test fname"""
        user = User()
        user.first_name = 'musee'
        self.assertEqual(user.first_name, 'musee')

    def test_user_lastname(self):
        """to test fname"""
        user = User()
        user.last_name = 'carter'
        self.assertEqual(user.last_name, 'carter')

    def test_to_dict(self):
        """test if they convert to dict"""
        user = User()
        user.email = 'mike@gmail.com'
        user.password = 'fd544'
        user.first_name = "musee"
        user.last_name = "carter"
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['email'], 'mike@gmail.com')
        self.assertEqual(user_dict['password'], 'fd544')
        self.assertEqual(user_dict['first_name'], 'musee')
        self.assertEqual(user_dict['last_name'], 'carter')


if __name__ == "__main__":
    unittest.main()
