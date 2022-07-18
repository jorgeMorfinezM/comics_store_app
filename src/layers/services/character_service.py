"""Define functionality on service layer"""
from __future__ import annotations

# from src.layers.domain.model.character import Character
from src.layers.domain.model.characters_response_dictionary import CharactersResponseDictionary
from src.layers.persistence.uow.domain_uow import DomainUOW
from src.layers.persistence.utils.character_serializer import CharacterSerializer
from src.layers.services.exceptions import BaseCustomException
from src.layers.services.exceptions import InvalidDictionaryFormat


class CharacterService:

    def __init__(self, character_uow: DomainUOW):
        self.character_uow = character_uow

    def get_sort_by_name_asc(self, params):
        """
        List

        :param: params: Dictionary or data to add
        to request Marvel API from the
        microservice endpoint requested
        """

        character_response = None

        response = self.character_uow.domain_repository.get(params)

        if len(response) <= 0:
            raise BaseCustomException('Response is Empty, verify the Marvel API endpoint on other service')

        try:

            character_response = [CharacterSerializer(character).character for character in response
                                  if type(CharactersResponseDictionary().__setitem__(1, character)) == dict]

            if character_response is not None:
                raise InvalidDictionaryFormat('Response does not have correct format')

        except InvalidDictionaryFormat as exc:
            print(exc)

        return character_response

    def get_by_name_start_with(self, params):
        """
        Get

        :param: params: Dictionary or data to add
        to request Marvel API from the
        microservice endpoint requested
        """

        response = self.character_uow.domain_repository.get(params)

        if len(response) <= 0:
            raise BaseCustomException('Response is Empty, verify the Marvel API endpoint on other service')

        return CharacterSerializer(response).character

    def get_by_name(self, params):
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

        return CharacterSerializer(response).character
