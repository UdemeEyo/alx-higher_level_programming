#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    msg = "arguments" if (length != 1) else "argument"
    msg += "." if (length == 0) else ":"

    print("{} {}".format(length, msg))
    for index, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(index + 1, arg))
