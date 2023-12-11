#!/usr/bin/python3
""" class user inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class for User attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
