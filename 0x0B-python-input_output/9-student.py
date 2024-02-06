#!/usr/bin/python3
"""For a class that defines a Student by some attributes
"""


class Student:
    """Defining a class for student with instance attributes"""

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method attrib to return directory representation of student"""
        return self.__dict__.copy()
