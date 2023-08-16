#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    numeral = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    number = numeral[roman_string[len(roman_string) - 1]]
    for i in range(len(roman_string) - 1, 0, -1):
        prev = numeral[roman_string[i - 1]]
        curr = numeral[roman_string[i]]

        if prev >= curr:
            number += prev
        else:
            number -= prev
    return number
