#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""


class BaseGeometry:
    """BaseGeometry instance"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """find area"""
        return self.__height * self.__width

    def __str__(self):
        """str"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
