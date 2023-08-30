#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, operand):
        """Equal to comparison"""
        return self.area() == operand.area()

    def __lt__(self, operand):
        """less than comparison"""
        return self.area() < operand.area()

    def __gt__(self, operand):
        """less than comparison"""
        return self.area() > operand.area()

    def __le__(self, operand):
        """less than or equalt to comparison"""
        return self.area() <= operand.area()

    def __ge__(self, operand):
        """greater than or equal to comparison"""
        return self.area() >= operand.area()

    def __ne__(self, operand):
        """not equal comparison"""
        return self.area() != operand.area()
