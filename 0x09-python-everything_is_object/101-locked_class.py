#!/usr/bin/python3
""" Defining a class - LockedClass. No class or object attribute.
"""


class LockedClass:
    __slots__ = ('first_name',)

    def __init__(self, first_name):
        self.first_name = first_name


locked_obj = LockedClass('Ultimate')
print(locked_obj.first_name)
