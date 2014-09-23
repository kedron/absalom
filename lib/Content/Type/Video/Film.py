""" Film.py - 
"""
from __future__ import absolute_import
from .Video import Video

class Film(Video):

    @property
    def release_date(self):
        return self._release_date

    @property
    def gross_us_revenues(self):
        return self._gross_us_revenues

    @property
    def gross_global_revenues(self):
        return self._gross_global_revenues

    @property
    def mpaa_rating(self):
        return self._mpaa_rating

    def __init__(self,
                 title=None,
                 producers=[],
                 directors=[],
                 screenwriters=[],
                 cinematographers=[],
                 actors=[]
                 ):
        self._title = title
        self._producers = producers
        self._directors = directors
        self._screenwriters = screenwriters
        self._cinematographers = cinematographers
        self._actors = actors
