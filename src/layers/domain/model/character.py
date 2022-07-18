"""This file intention is to provide the class Comics and its business rules"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Character:
    """Comic model to looking for data from API Client requested"""

    id: int
    name: str
    image: str
    appearances: int
