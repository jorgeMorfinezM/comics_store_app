"""This file has the purpose of serving to serialize a cat fact response to json format"""
from __future__ import annotations

from marshmallow import fields
from marshmallow import Schema


class ComicSchema(Schema):
    id: fields.Integer()
    title: fields.String()
    image: fields.String()
    on_sale_date = fields.String()
