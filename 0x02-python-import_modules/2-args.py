#!/usr/bin/python3
if __name__ == "__main__":
    """Print out list and num of arguments."""
    import sys

    guo = len(sys.argv) - 1
    if guo == 0:
        print("0 arguments.")
    elif guo == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(guo))
    for start in range(guo):
        print("{}: {}".format(start + 1, sys.argv[start + 1]))
