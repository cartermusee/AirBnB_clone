#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State

"""class for testing state"""


class TestReview(unittest.TestCase):
    """class to test"""

    def test_inheritance(self):
        """test inheritance"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_name(self):
        """to name"""
        state = State()
        state.name = 'miami'
        self.assertEqual(state.name, 'miami')

    def test_to_dict(self):
        """test if they convert to dict"""
        state = State()
        state.name = 'miami'
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['name'], 'miami')


if __name__ == "__main__":
    unittest.main()
