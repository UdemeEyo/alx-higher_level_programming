#!/usr/bin/python3
"""
A class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherit from BaseGeometry
    """

    def __init__(self, size):
        """
        The constructor function
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        string changes the representation
        """
        return ('[square]' + str(self.width) + '/' + str(self.height))
