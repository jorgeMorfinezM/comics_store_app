"""..."""
from __future__ import annotations

from config import LOOKING_FOR_CRITERIA_ACCEPTANCE

from flask_api import status

from src.layers.domain.model.comic import Comic
from src.layers.domain.model.character import Character
from src.layers.http_api.bridge.serializer.json.character_schema import CharacterSchema
from src.layers.http_api.bridge.serializer.json.comic_schema import ComicSchema
from src.layers.services.character_service import CharacterService
from src.layers.services.comic_service import ComicService


class ViewRequestHandler:
    """..."""

    def __init__(self, character_service: CharacterService, character_model: Character,
                 comic_service: ComicService, comic_model: Comic) -> None:
        self.character_service = character_service
        self.character_schema = CharacterSchema()
        self.character_model = character_model

        self.comic_service = comic_service
        self.comic_schema = ComicSchema()
        self.comic_model = comic_model

    @staticmethod
    def pagination(list_of_entities, sample_range):
        """..."""

        return [list_of_entities[i:i + sample_range] for i in range(0, len(list_of_entities), sample_range)]

    @staticmethod
    def pagination_response(list_of_entities, page):
        """..."""

        if page <= 0:
            raise Exception('Page cant be zero or negative')

        pages = len(list_of_entities)

        list_of_entities = list_of_entities[int(page) - 1]

        return {'pages': pages, 'resource': list_of_entities}

    def search_comics(self, search_term, page, showing_range, params):
        """..."""

        try:

            if search_term:
                if search_term in LOOKING_FOR_CRITERIA_ACCEPTANCE:

                    if "personajes" == search_term:
                        # Metodo que llama a endpoint de character o comic
                        character_response = self.character_service.get_by_name(params=params)

                        return character_response, status.HTTP_200_OK

                    elif "comics" == search_term:
                        # Metodo que llama a endpoint de listar all Characters ordered by name
                        comic_response = self.comic_service.get_by_title(params=params)

                        return comic_response, status.HTTP_200_OK
            else:
                # Metodo que llama a endpoint de listar personajes por nombre ascendente
                list_of_characters = self.character_service.get_sort_by_name_asc(params=params)

                list_of_characters = [
                    self.character_schema.dump(characters) for characters in list_of_characters
                ]

                list_of_characters = self.pagination(list_of_characters, int(showing_range))

                paginated_response = self.pagination_response(list_of_characters, int(page))

                return paginated_response, status.HTTP_200_OK

        # pylint: disable=broad-except
        except Exception as exc:
            return {'error': exc.args[0]}, status.HTTP_400_BAD_REQUEST
