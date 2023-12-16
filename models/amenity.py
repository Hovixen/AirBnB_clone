#!/usr/bin/python3
"""
inherints from class BaseModel
Public class attributes:
    name: string - empty string
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class Amenity """

    name = ""

    def __init__(self, *args, **kwargs):
        """ initializing amenity """
        super().__init__(*args, **kwargs)
