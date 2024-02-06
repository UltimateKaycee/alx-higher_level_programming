#!/usr/bin/python3
"""For a script that reads from stdin and computes metrics.

"""


def print_stats(size, status_codes):
    """Declaration that prints metrics.

    Arguments are size (int): file size and
        status_codes (dict): status codes.
    """
    print("File size: {}".format(size))
    for loom in sorted(status_codes):
        print("{}: {}".format(loom, status_codes[loom]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    main_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    number = 0

    try:
        for item in sys.stdin:
            if number == 10:
                print_stats(size, status_codes)
                number = 1
            else:
                number += 1

            item = item.split()

            try:
                size += int(item[-1])
            except (IndexError, ValueError):
                pass

            try:
                if item[-2] in main_codes:
                    if status_codes.get(item[-2], -1) == -1:
                        status_codes[item[-2]] = 1
                    else:
                        status_codes[item[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
