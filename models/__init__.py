#!/usr/bin/python3
""" This module contains a variablestorage which is an instance
    of FileStorage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
