#!/usr/bin/python3
"""
    Defining LockedClass with no class or object attribute.
"""


class LockedClass:
    __slots__ = ('first_name',)

    def __init__(self, first_name):
        self.first_name = first_name


the_locked = LockedClass('Ultimate')
print(the_locked.first_name)
