#!/usr/bin/python3


"""
inherits from class BaseModel
    Public class attributes:
        name: string - empty string
"""


from models.base_model import BaseModel


class State(BaseModel):
    """ class State """

    name = ""

    def __init__(self, *args, **kwargs):
        """ initializing state """
        super().__init__(*args, **kwargs)
