""" Content.py - Base Class
"""
from __future__ import absolute_import

class Content(object):

    @property
    def title(self):
        return self._title

    @property
    # form of content, e.g. video, audio, etc.
    def form(self):
        return self._type

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
                 content_type=None,
                 storage=None
                ):
        self._title = title
        self._content_type = type
        self._storage = storage
