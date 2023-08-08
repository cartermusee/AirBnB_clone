#!/usr/bin/python3
from models.base_model import BaseModel
"""class user"""


class User(BaseModel):
    """public attributes of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
