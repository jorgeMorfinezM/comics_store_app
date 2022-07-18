"""Custom data structure that allow ComicsResponseDictionary"""
from __future__ import annotations

from src.layers.domain.model.comic import Comic
from src.layers.domain.exceptions import IsNotModelError
from src.layers.domain.model.utils.base_dictionary import BaseDictionary


class ComicsResponseDictionary(BaseDictionary):
    """CharactersResponseDictionary its a custom data structure that allow Character"""

    def __setitem__(self, key, item: Comic):
        if not isinstance(item, Comic):
            raise IsNotModelError('Value it is not Character model')
        self.__dict__[key] = item
