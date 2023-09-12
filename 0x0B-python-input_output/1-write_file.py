#!/usr/bin/python3

"""writes a string to a text file (UTF8) and returns
the number of characters written"""


def write_file(filename="", text=""):
    """writes to a UTF-8 encoded file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
