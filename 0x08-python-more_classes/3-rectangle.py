#!/usr/bin/python3

""" A  class Rectangle that defines a rectangle"""


class Rectangle:
    """Create a Rectangle Instance"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ""
        res = []

        for i in range(self.__height):
            [res.append("#") for n in range(self.width)]
            if i != self.__height - 1:
                res.append("\n")
        return "".join(res)
