# FileSystem.py - 
from __future__ import absolute_import
import os
import sys

""" Filesystem Structure

    DATA_DIR - top level directory 


"""

class FileSystem(object):


    @property
    def data_directory(self):
        """ top-level filesystem path where data files and links are stored
        """
        return self._data_directory

    def __init__(self,
                 data_directory=None):
        _data_directory = data_directory

    
    def findMedia(self,
                  types=None,
                  genres=None,
                 ):
        pass
