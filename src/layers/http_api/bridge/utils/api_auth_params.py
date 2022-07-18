'''This file intention is to provide the other user type classes with a
base and avoid code duplication'''
from __future__ import annotations

import time
import calendar
import hashlib
from config import MARVEL_API_PRIVATE_KEY
from config import MARVEL_API_PUBLIC_KEY


class APIAuthParams:

    ts: float
    _hash: str
    api_key_private: str
    api_key_public: str

    def __post_init__(self):
        self.__initialize()

    def __initialize(self):
        # Getting the current date and time
        # dt = datetime.now()

        # getting the timestamp
        # self.ts = datetime.timestamp(dt)

        self.api_key_public = MARVEL_API_PUBLIC_KEY

        self.api_key_private = MARVEL_API_PRIVATE_KEY

        # Current GMT time in a tuuple format
        current_gmt = time.gmtime()

        # ts stores timestamp
        self.ts = calendar.timegm(current_gmt)

        self._hash = str(self.ts) + self.api_key_private + self.api_key_public

    @property
    def hash(self):
        return hashlib.md5(str(self._hash).encode('utf-8')).hexdigest()

    @hash.setter
    def hash(self, str_to_hash):
        self._hash = str_to_hash


