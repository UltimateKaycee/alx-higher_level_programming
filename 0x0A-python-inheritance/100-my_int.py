#!/usr/bin/python3
"""Class definition for MyInt which inherits from int."""


class MyInt(int):
    """The class definition"""

    def __eq__(self, value):
        """Function to override == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """Function to override != operator with ==."""
        return self.real == value
