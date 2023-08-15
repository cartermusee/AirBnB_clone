#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review

"""class for testing reviews"""


class TestReview(unittest.TestCase):
    """tests Review """

    def test_inheritance(self):
        """test inheritance"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_place_id(self):
        """test pl id"""
        rev = Review()
        rev.id = "342"
        self.assertEqual(rev.id, '342')

    def test_user_id(self):
        """to test user id"""
        revuserid = Review()
        revuserid.user_id = '544'
        self.assertEqual(revuserid.user_id, '544')

    def test_user_text(self):
        """to test user text """
        revuserid = Review()
        revuserid.text = 'nice how are you'
        self.assertEqual(revuserid.text, 'nice how are you')

    def test_to_dict(self):
        """test if they convert to dict"""
        rev = Review()
        rev.user_id = '544'
        rev.text = 'how are you'
        rev.place_id = "33344"
        rev_dict = rev.to_dict()
        self.assertIsInstance(rev_dict, dict)
        self.assertEqual(rev_dict['user_id'], '544')
        self.assertEqual(rev_dict['text'], 'how are you')
        self.assertEqual(rev_dict['place_id'], '33344')


if __name__ == "__main__":
    unittest.main()
