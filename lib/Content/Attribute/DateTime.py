""" DateTime.py - 
"""

class DateTime(object):

    @property
    def release_date(self):
        return self._release_date

    @property
    def create_time(self):
        return self._create_time

    @property
    def update_time(self):
        return self._update_time

    def __init__(self,
                 release_date = None,
                 create_time = None,
                 update_time = None,
                ):
        _release_date = release_date
        _create_time = create_time
        _update_time = update_time

    
