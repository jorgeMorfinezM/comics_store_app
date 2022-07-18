"""API Client"""
from __future__ import annotations

import requests

from src.layers.persistence.base_persistence import Config
from src.layers.persistence.base_persistence import APIConnect


class APIConfig(Config):

    def __init__(self, url_host, endpoint, http_method, headers, search_term_param):
        super().__init__(url_host, endpoint, http_method, headers, search_term_param)

        self.url_host = url_host
        self.endpoint = endpoint
        self.http_method = http_method
        self.headers = headers
        self.search_term_param = search_term_param


class APIClient(APIConnect):
    """
    Setting up API Client and set methods to
    get connection and requested endpoint
    """

    response = None

    def __init__(self, api_config: APIConfig):
        super().__init__(api_config)

        self.api_config = api_config

    def request(self, params):
        """
        Method connect to setup API configuration and requested endpoint

        :param: params: Arguments to parte on the requested endpoint.
        :return: self.response: Response API requested endpoint object
        """

        if params is not None:

            self.response = requests.request(method=self.api_config.http_method,
                                             url=self.api_config.url_host,
                                             headers=self.api_config.headers,
                                             params=params)

        return self.response
