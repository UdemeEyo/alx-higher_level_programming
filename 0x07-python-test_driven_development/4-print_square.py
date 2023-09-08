#!/usr/bin/python3

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    rect = []
    for n in range(size):
        [rect.append("#") for i in range(size)]
        if n != size - 1:
            rect.append("\n")
    print("".join(rect))
