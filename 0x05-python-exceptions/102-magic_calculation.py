#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0
    for start in range(1, 3):
        try:
            if start > a:
                raise Exception('Exceeded range')
            else:
                output += a ** b / start
        except Exception as dead:
            output = a + b
            break
    return (output)
