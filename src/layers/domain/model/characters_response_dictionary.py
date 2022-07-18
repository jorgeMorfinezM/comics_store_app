"""Custom data structure that allow CharactersResponseDictionary"""
from __future__ import annotations

from  src.layers.domain.model.character import Character
from src.layers.domain.exceptions import IsNotModelError
from src.layers.domain.model.utils.base_dictionary import BaseDictionary


class CharactersResponseDictionary(BaseDictionary):
    """CharactersResponseDictionary its a custom data structure that allow Character"""

    def __setitem__(self, key, item: Character):
        if not isinstance(item, Character):
            raise IsNotModelError('Value it is not Character model')
        self.__dict__[key] = item
