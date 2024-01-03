#!/usr/bin/python3
""""Print the alphabet in reverse order alternating upper- and lower-case."""
start = 0
for count in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(count - start)), end="")
    start = 32 if start == 0 else 0
