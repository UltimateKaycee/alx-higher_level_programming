#!/usr/bin/python3
"""Class definition for inherited list."""


class MyList(list):
    """For cklass that inherits from list."""

    def print_sorted(self):
        """Function prints a lis sorted in ascending order."""
        print(sorted(self))
