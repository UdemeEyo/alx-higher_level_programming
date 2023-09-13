#!/usr/bin/python3

"""appends a string to a text file (UTF8) and returns
the number of characters written"""


def append_write(filename="", text=""):
    """writes to a UTF-8 encoded file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
