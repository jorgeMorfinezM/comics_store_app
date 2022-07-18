'''Intention: Handle http request'''
from __future__ import annotations

import abc


class AbstractRequestHandlerMethods(abc.ABC):
    """Abstract class with the purpose of manage
    and handle http request isnt mandatory to use all methods"""

    @abc.abstractmethod
    def get(self, request):
        """GET: Read"""
