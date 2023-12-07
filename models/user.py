#!/usr/bin/python3
""" class user inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """ class User"""
    def __init__(self, *args, **kwargs):
        """initialization of User class"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")

    def to_dict(self):
        """store user details to dictionary"""
        user_dict = super().to_dict()
        user_dict.update({
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
            })
        return user_dict
