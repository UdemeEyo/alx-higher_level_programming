#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = 0
    while n < len(text) and text[n] == " ":
        n += 1

    while n < len(text):
        print(text[n], end="")
        if text[n] == "\n" or text[n] in "?.:":
            if text[n] in "?.:":
                print("\n")
            n += 1
           
            while n < len(text) and text[n] == " ":
                n += 1
            continue
        n += 1
