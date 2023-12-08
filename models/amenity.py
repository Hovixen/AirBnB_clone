#!/usr/bin/python3


"""
inherits from class BaseModel
Public class attributes:
    name: string - empty string
"""


class Amenity(BaseModel):
    """ class Amenity """

    name = ""

    def __init__(self, *args, **kwargs):
        """ initializing amenity """
        super().__init__(*args, **kwargs)
