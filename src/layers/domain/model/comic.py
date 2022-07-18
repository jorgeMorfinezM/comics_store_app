"""This file intention is to provide the class Comics and its business rules"""
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime


@dataclass
class Comic:
    """Comic model to looking for data from API Client requested"""

    id: int
    title: str
    image: str
    on_sale_date: datetime = field(init=False)
