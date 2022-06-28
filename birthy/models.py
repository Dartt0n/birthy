from __future__ import annotations
from datetime import datetime
from tortoise import fields
from tortoise.models import Model
from loguru import logger


class Group(Model):
    telegram_id = fields.BigIntField(pk=True)
    timezone = fields.CharField(50, default="Europe/Moscow")
    do_tag = fields.BooleanField(default=False)
    do_remind_in_day = fields.BooleanField(default=False)
    remind_in_day = fields.IntField()

    @classmethod
    async def by_id(cls, telegram_id: int) -> Group | None:
        return await cls.filter(telegram_id=telegram_id).get_or_none()


class Person(Model):
    telegram_id = fields.BigIntField(pk=True)
    name = fields.CharField(255)
    date = fields.DateField()
    group = fields.ForeignKeyField("models.Group", related_name="persons")

    @classmethod
    async def by_id(cls, telegram_id: int) -> Person | None:
        return await cls.filter(telegram_id=telegram_id).get_or_none()

    @property
    def days_before_birthday(self):
        return (self.date - datetime.now().date().replace(year=1900)).days  # type: ignore
