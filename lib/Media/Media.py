""" Media.py - Base Class
"""
from __future__ import absolute_import

class Media(object):

    @property
    def title(self):
        return self._title

    @property
    def physical_storage(self):
        return self._physical_storage

    @property
    def creation_time(self):
        return self._creation_time

    @property
    def last_update_time(self):
        return self._last_update_time

    def __init__(self, 
                 title=None,
                 storage=None
                ):
        self._title = title
        self._storage = storage
