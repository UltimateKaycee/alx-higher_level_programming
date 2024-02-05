#!/usr/bin/python3
"""Class definition for base geometry."""


class BaseGeometry:
    """Class for base geometry."""

    def area(self):
        """Will raise exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Will perform integer validation on parameter.

        Arguments are name (str) of parameter and value (int) to validate.
        Returns TypeError if value not integer or ValueError if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
