#!/usr/bin/python3
"""
inherits from class BaseModel
Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ class City """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializing City """
        super().__init__(*args, **kwargs)
