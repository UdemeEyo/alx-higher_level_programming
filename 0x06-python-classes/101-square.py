#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print("")

    def __str__(self):
        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for i in range(self.__position[0])]
            [print("#", end="") for i in range(self.__size)]
            if i != self.size - 1:
                print("")
        return ""
