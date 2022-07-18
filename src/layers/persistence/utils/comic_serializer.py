'''This file intention is to provide serializer for Comic'''
from __future__ import annotations

from src.layers.domain.model.comic import Comic


class ComicSerializer:
    """This serializer has the purpose of setting requested dictionaries
        to domain object, in this case to a comic"""

    def __init__(self, response: dict):

        self.comic = Comic(0, '', '')

        self.comic.id = response['data']['results'].get('id')
        self.comic.title = response['data']['results'].get('title')
        self.comic.image = response['data']['results'].get('images')['path']

        if "onsaleDate" in response['data']['results'].get('dates')['type']:
            self.comic.on_sale_date = response['data']['results'].get('dates')['date']
