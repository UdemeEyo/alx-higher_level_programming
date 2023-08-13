#!/usr/bin/python3

newstr = ""
count = 1
for c in range(ord('z'), ord('a') - 1, -1):
    if (count % 2 == 0):
        newstr += chr(c - 32)
    else:
        newstr += chr(c)
    count += 1
print("{}".format(newstr), end="")
