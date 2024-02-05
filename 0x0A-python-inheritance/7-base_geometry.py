#!/usr/bin/python3
"""Class definition for a base geometry class BaseGeometry."""


class BaseGeometry:
    """Defines the class base geometry."""

    def area(self):
        """Function raises exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method validate parameter as integer.

        Arguments are name (str) of parameter.
            value (int) parameter to validate.
        Raises TypeError if value isn't integer
        and ValueError if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
