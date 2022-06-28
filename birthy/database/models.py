from __future__ import annotations  # better typing
from datetime import datetime
from tortoise import fields as db
from tortoise.models import Model


class Group(Model):
    """class representing a telegram group"""

    telegram_id = db.IntField(pk=True)
    remind_interval = db.IntField()


class Person(Model):
    """class representing a telegram user"""

    telegram_id = db.IntField(pk=True)
    name = db.CharField(255)
    birth_date = db.DateField()
    group = db.ForeignKeyField("models.Group", related_name="persons")
