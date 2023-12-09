#!/usr/bin/python3

from models.base_model import BaseModel
"""
inherits from class BaseModel
Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
"""


class Review(BaseModel):
    """ class Review """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initializing Review """
        super().__init__(*args, **kwargs)
