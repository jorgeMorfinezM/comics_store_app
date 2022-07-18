"""This file has the purpose of serving to serialize a cat fact response to json format"""
from __future__ import annotations

from marshmallow import fields
from marshmallow import Schema


class CharacterSchema(Schema):
    id: fields.Integer()
    name: fields.String()
    image: fields.String()
    appearances = fields.String()
