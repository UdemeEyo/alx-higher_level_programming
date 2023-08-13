#!/usr/bin/python3

def remove_char_at(str, n):
    newstr = ""
    for idx, c in enumerate(str):
        if idx == n:
            continue
        newstr += c
    return newstr
