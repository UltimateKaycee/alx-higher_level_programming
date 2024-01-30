#!/usr/bin/python3
"""Module for a function of text-indentation."""

def text_indentation(text):
    """Function to print text with two new lines after '.', '?', and ':'.

    Arguments - text (string): Output text.
    Will return TypeError if text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cha = 0
    while cha len(text) and text[cha] == ' ':
        cha += 1

    while cha < len(text):
        print(text[cha], end="")
        if text[cha] == "\n" or text[cha] in ".?:":
            if text[cha] in ".?:":
                print("\n")
            cha += 1
            while cha < len(text) and text[cha] == ' ':
                cha += 1
            continue
        cha += 1
