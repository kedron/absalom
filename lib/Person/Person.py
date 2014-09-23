""" Person.py
"""

class Person:

    @property
    def display_name(self):
        return _display_name

    def __init__(self,
                 display_name = None,
                ):
        _display_name = display_name
