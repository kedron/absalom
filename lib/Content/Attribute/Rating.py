""" Attribute.py - Abstract Base Class
"""

class Attribute(object):

    @property
    def rotten_tomatoes(self):
        return self._rotten_tomatoes

    @property
    def metacritic(self):
        return self._metacritic

    @property
    def imdb(self):
        return self._imdb

    def __init__(self,
                 rotten_tomatoes = None,
                 metacritic = None,
                 imdb = None,
                ):
        _rotten_tomatoes = rotten_tomatoes
        _metacritic = metacritic
        _imdb = imdb
