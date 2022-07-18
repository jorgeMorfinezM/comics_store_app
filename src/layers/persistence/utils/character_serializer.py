'''This file intention is to provide serializer for Character'''
from __future__ import annotations

from src.layers.domain.model.character import Character


class CharacterSerializer:
    """This serializer has the purpose of setting requested dictionaries
        to domain object, in this case to a character"""

    def __init__(self, response: dict):

        self.character = Character(0, '', '', 0)

        self.character.id = response['data']['results'].get('id')
        self.character.name = response['data']['results'].get('name')
        self.character.image = response['data']['results'].get('thumbnail')['path']
        self.character.appearances = response['data']['results'].get('comics')['available']
