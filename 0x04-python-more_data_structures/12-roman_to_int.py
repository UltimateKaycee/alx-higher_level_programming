#!/usr/bin/python3

def roman_to_int(roman_string):
    """Function to convert roman numeral to int."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    col = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0

    for start in range(len(roman_string)):
        if col.get(roman_string[start], 0) == 0:
            return (0)

        if (start != (len(roman_string) - 1) and
                col[roman_string[start]] < col[roman_string[start + 1]]):
            number += col[roman_string[start]] * -1

        else:
            number += col[roman_string[start]]
    return (number)
