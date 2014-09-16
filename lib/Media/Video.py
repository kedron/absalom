""" Video.py - 
"""
from __future__ import absolute_import
from .Media import Media

class Video(Media):

    @property
    def studio(self):
        return self._studio

    @property
    def producers(self):
        return self._producers
    def add_producer(self, producer):
        self._producers.append(producer)
        return self._producers

    @property
    def directors(self):
        return self._directors
    def add_director(self, director):
        self._directors.append(director)
        return self._directors

    @property
    def screenwriters(self):
        return self._screenwriters
    def add_screenwriter(self, screenwriter):
        self._screenwriters.append(screenwriter)
        return self._screenwriters

    @property
    def cinematographers(self):
        return self._cinematographers
    def add_cinematographer(self, cinematographer):
        self._cinematographers.append(cinematographer)
        return self._cinematographers

    @property
    def actors(self):
        return self._actors
    def add_actor(self, actor):
        self._actors.append(actor)
        return self._actors

    @property
    def genres(self):
        return self._genres
    def add_genre(self, genre):
        self._genres.append(genre)
        return self._genres

    @property
    def critical_ratings(self):
        return self._critical_ratings
    def add_critical_rating(self, critical_rating):
        self._critical_ratings.append(critical_rating)
        return self._critical_ratings

    @property
    def resolution(self):
        return self._resolution

    @property
    def length(self):
        return self._resolution

    def __init__(self,
                 title=None,
                 producers=[],
                 directors=[],
                 screenwriters=[],
                 cinematographers=[],
                 actors=[]
                ):
        
        super(Video, self).__init__(title)
        self._producers = producers
        self._directors = directors
        self._screenwriters = screenwriters
        self._cinematographers = cinematographers
        self._actors = actors
