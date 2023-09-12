#!/usr/bin/python3
"""
MyList inherit from list
"""


class list:
    """
    The super class list
    """
    def __init__(self, list):
        """
        The init function is the constructor function taking the parameter list
        """
        self.list = list


class MyList(list):
    """
    Mylist has inherited list into it class
    """
    def __init__(self, list):
        """
        It is the constructor function
        """
        super().__init__()

    def print_sorted(self):
        """
        It returns the sorted list of the original list
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
