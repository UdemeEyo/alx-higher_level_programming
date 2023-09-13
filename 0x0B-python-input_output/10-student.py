#!/usr/bin/python3

"""My module"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Creates a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student Dictionary"""
        if attrs is None:
            return self.__dict__
        ndict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                ndict[key] = value
        return ndict
