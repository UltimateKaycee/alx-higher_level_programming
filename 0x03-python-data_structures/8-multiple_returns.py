#!/usr/bin/python3
def multiple_returns(sentence):
    the_length = len(sentence)
    char_one = sentence[0] if the_length > 0 else "None"
    the_tup = the_length, char_one
    return(the_tup)
