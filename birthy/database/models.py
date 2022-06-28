from __future__ import annotations  # better typing
import pytz
from datetime import datetime, date

from tortoise import fields as db
from tortoise.models import Model


class Group(Model):
    """class representing a telegram group"""

    telegram_id = db.IntField(pk=True)
    timezone = db.CharField(50)
    remind_interval = db.IntField()

    persons: db.ReverseRelation["Person"]


class Person(Model):
    """class representing a telegram user"""

    telegram_id = db.IntField(pk=True)
    name = db.CharField(255)
    birth_date = db.DateField()
    group = db.ForeignKeyField("models.Group", related_name="persons")

    async def days_before_birthday(self):
        await self.fetch_related("group")
        now = pytz.timezone(self.group.timezone).localize(datetime.today()).date()
        this_year = date(now.year, self.birth_date.month, self.birth_date.day)
        next_year = date(now.year + 1, self.birth_date.month, self.birth_date.day)
        return ((this_year if this_year > now else next_year) - now).days
