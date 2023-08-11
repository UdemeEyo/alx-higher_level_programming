#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    for b in argv[1:]:
        a += int(b)
    print("{:d}".format(a))
