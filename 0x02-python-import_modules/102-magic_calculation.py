#!/usr/bin/python3
def magic_calculation(a, b):
    """Match the provided bytecode."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for start in range(4, 6):
            c = add(c, start)
        return (c)

    else:
        return(sub(a, b))
