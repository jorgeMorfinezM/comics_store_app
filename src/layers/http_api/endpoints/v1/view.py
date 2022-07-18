"""..."""
# mypy: ignore-errors
from __future__ import annotations

import json
from urllib.parse import urlencode
from flask import Blueprint
from flask import request
import config
from src.layers.domain.model.comic import Comic
from src.layers.domain.model.character import Character
from src.adapters.persistence.api_client import APIClient
from src.adapters.persistence.api_client import APIConfig
from src.layers.http_api.bridge.controller.view_request_handler import ViewRequestHandler
from src.layers.persistence.uow.domain_uow import DomainUOW
from src.layers.services.character_service import CharacterService
from src.layers.services.comic_service import ComicService
from src.layers.http_api.bridge.utils.api_auth_params import APIAuthParams

endpoint_blueprint = Blueprint('searchComics', __name__, url_prefix='/v1/searchComics')


def _initialize_params(search_term, search_param):

    params_endpoint_request = None

    if search_term:

        params = {}

        if "personajes" in search_term:
            if len(search_param) <= 2:
                params.update({"nameStartsWith": search_param})

            params.update({"name": search_param})

        elif "comics" in search_term:
            if len(search_param) <= 2:
                params.update({"titleStartsWith": search_param})

            params.update({"title": search_param})

        # search_term=<search_term>&search_param=<search_param>
        params_endpoint_request = urlencode(params)
        # params_endpoint_request = query_string_transform._get_query_string(params)

    return params_endpoint_request


def _build_request_params(search_term, search_param, page, showing_range):

    hash_param = APIAuthParams.hash
    ts_param = APIAuthParams.ts
    auth_api_key = APIAuthParams.api_key_public

    auth_params = {
        "hash": hash_param,
        "ts": ts_param,
        "apiKey": auth_api_key,

    }

    request_auth = urlencode(auth_params)

    params_init = _initialize_params(search_term, search_param)

    sorted_params = {"page": page,
                     "showing_range": showing_range}

    sorted_params = urlencode(sorted_params)

    all_params_endpoint = params_init

    if sorted_params:
        all_params_endpoint += "&" + sorted_params

    endpoint_params = params_init + "&" + request_auth

    return endpoint_params


def _build_search_request(search_term, search_param, page, showing_range):
    endpoint_request = None
    characters_services = None
    comics_services = None
    character_model = None
    comic_model = None

    endpoint_params = _build_request_params(search_term, search_param, page, showing_range)

    url_host = config.MARVEL_URL_HOST
    http_method = 'GET'
    headers = config.HEADERS

    if not search_term:

        endpoint_request = config.ENDPOINT_CHARACTERS_ORDERBY_NAME

        api_config = APIConfig(url_host, endpoint_request, http_method, headers, endpoint_params)

        api_client = APIClient(api_config)

        characters_services = CharacterService(DomainUOW(url_host,
                                                         endpoint_request,
                                                         http_method,
                                                         headers,
                                                         search_param,
                                                         api_client))

        character_model: Character

    else:
        if "personajes" in search_term:
            if len(search_param) <= 2:
                endpoint_request = config.ENDPOINT_CHARACTERS_START_NAME

            endpoint_request = config.ENDPOINT_CHARACTERS_BY_NAME

            api_config = APIConfig(url_host, endpoint_request, http_method, headers, endpoint_params)

            api_client = APIClient(api_config)

            characters_services = CharacterService(DomainUOW(url_host,
                                                             endpoint_request,
                                                             http_method,
                                                             headers,
                                                             search_param,
                                                             api_client))

            character_model: Character

        elif "comics" in search_term:
            if len(search_param) <= 2:
                endpoint_request = config.ENDPOINT_COMIC_START_TITLE

            endpoint_request = config.ENDPOINT_COMIC_BY_TITLE

            api_config = APIConfig(url_host, endpoint_request, http_method, headers, endpoint_params)

            api_client = APIClient(api_config)

            comics_services = ComicService(DomainUOW(url_host,
                                                     endpoint_request,
                                                     http_method,
                                                     headers,
                                                     search_param,
                                                     api_client))

            comic_model: Comic

    request_handler = ViewRequestHandler(characters_services, character_model,
                                         comics_services, comic_model)

    return request_handler


@endpoint_blueprint.get('/')
def search_comics():
    """.."""

    page = request.args.get('page')
    showing_range = request.args.get('showing_range')

    search_term = request.args.get('searchTerm')
    search_param = None

    if "personajes" == search_term:
        search_param = request.args.get('name')
    elif "comics" == search_term:
        search_param = request.args.get('title')

    params = _build_request_params(search_term, search_param, page, showing_range)

    request_handler = _build_search_request(search_term, search_param, page, showing_range)

    response = request_handler.search_comics(search_term, page, showing_range, params)

    return response
