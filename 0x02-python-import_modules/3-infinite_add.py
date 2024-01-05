#!/usr/bin/python3
if __name__ == "__main__":
    """Print out sum of arguments."""
    import sys

    sum = 0
    for start in range(len(sys.argv) - 1):
        sum += int(sys.argv[start + 1])
    print("{}".format(sum))
