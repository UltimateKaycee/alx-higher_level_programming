#!/usr/bin/python3
def remove_char_at(str, abb):
    """Create a copy of the string without the character at position n."""
    if abb < 0:
        return (str)
    return (str[:abb] + str[abb+1:])
