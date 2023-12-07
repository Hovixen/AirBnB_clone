#!/usr/bin/python3
""" serialization and deserialization of instances to & from json"""


import json


class FileStorage():
    """ class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ assigns objects """
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save objects to json file """
        dic = {}
        for key, obj in self.__objects.items():
            dic[key] = obj.to_dict()
        with open(self.__file_path, mode = "w", encoding = "utf-8") as file:
            json.dump(dic, file)

    def reload(self):
        """ loads objects from file """
        try:
            with open(self.__file_path, mode = "r", encoding = "utf-8") as file:
                new = json.load(file)
                for key, obj_dict in new.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
