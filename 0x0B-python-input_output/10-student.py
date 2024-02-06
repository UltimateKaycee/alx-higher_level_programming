#!/usr/bin/python3
"""For a class that defines a student
"""


class Student:
    """Defining a class to create instances of student"""

    def __init__(self, first_name, last_name, age):
        """Initialize instance method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Instance method to return directory rep"""
        the_object = self.__dict__.copy()
        if type(attrs) is list:

            for elem in attrs:
                if type(elem) is not str:
                    return the_object

            listing = {}

            for bim in range(len(attrs)):
                for bam in the_object:
                    if attrs[bim] == bam:
                        listing[bam] = the_object[bam]
            return listing

        return the_object
