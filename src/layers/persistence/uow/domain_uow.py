"""This file intention is to provide uow for CatFacts"""
from __future__ import annotations

from src.adapters.persistence.api_client import APIClient
from src.layers.persistence.base_uow import AbstractUnitOfWork
from src.layers.persistence.repository.domain_repository import DomainRepository


class DomainUOW(AbstractUnitOfWork):
    """Implementation of the abstract class of unit of work
       with implementation of magic methods"""

    def __init__(self, url_host, endpoint, http_method, headers, search_type, api_client: APIClient):
        self.api_client = api_client

        self.api_client.api_config.url_host = url_host
        self.api_client.api_config.endpoint = endpoint
        self.api_client.api_config.http_method = http_method
        self.api_client.api_config.headers = headers
        self.search_type = search_type

        self.domain_repository = DomainRepository(self.api_client)

    def __enter__(self, params):
        # pylint: disable=attribute-defined-outside-init
        self.api_client.request(params)
        return super().__enter__()
