#!/usr/bin/python3
if __name__ == "__main__":
    """Print sum of arguments."""
    import sys

    all = 0
    for start in range(len(sys.argv) - 1):
        all += int(sys.argv[start + 1])
    print("{}".format(all))
