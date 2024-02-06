#!/usr/bin/python3
"""For class that defines a Student based on a module
"""


class Student:
    """defining a class to create instance of student"""

    def __init__(self, first_name, last_name, age):
        """Initializing instance method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class method to return directory representation"""
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

    def reload_from_json(self, json):
        """Will replace attributes of Student instance"""
        for atr_one in json:
            self.__dict__[atr_one] = json[atr_one]
