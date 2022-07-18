"""Define functionality on service layer"""
from __future__ import annotations

# from src.layers.domain.model.comic import Comic
# from src.layers.domain.model.comics_response_dictionary import ComicsResponseDictionary
from src.layers.persistence.uow.domain_uow import DomainUOW
from src.layers.persistence.utils.comic_serializer import ComicSerializer
from src.layers.services.exceptions import BaseCustomException
# from src.layers.services.exceptions import InvalidDictionaryFormat


class ComicService:

    def __init__(self, character_uow: DomainUOW):
        self.character_uow = character_uow

    def get_by_title_start_with(self, params):
        """
        Get

        :param: params: Dictionary or data to add
        to request Marvel API from the
        microservice endpoint requested
        """

        response = self.character_uow.domain_repository.get(params)

        if len(response) <= 0:
            raise BaseCustomException('Response is Empty, verify the Marvel API endpoint on other service')

        return ComicSerializer(response).comic

    def get_by_title(self, params):
        """
        Get Characters filtered by Name attribute
        from Marvel API requested

        :param: params: Dictionary or data to add
        to request Marvel API from the
        microservice endpoint requested
        """

        response = self.character_uow.domain_repository.get(params)

        if len(response) <= 0:
            raise BaseCustomException('Response is Empty, verify the Marvel API endpoint on other service')

        return ComicSerializer(response).comic
