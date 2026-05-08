from peewee import *
from enum import IntEnum
from ..config import db


class Session(IntEnum):
    LOGGED_IN = 0
    LOGGED_OUT = 1

class BaseModel(Model):
    class Meta:
        database = db

class Profile(BaseModel):

    username = CharField()
    bio = TextField()

    session = IntegerField(default=Session.LOGGED_OUT)
    join_date = CharField()

    @property
    def session_status(self):
        return Session(self.session)

    @session_status.setter
    def session_status(self, value):
        self.session = int(value)

    class Meta:
        table_name = "profile"


class Friend(Profile):
    profile = ForeignKeyField(Profile, backref='friends', column_name='profile_id')
    tag = CharField()

    class Meta:
        table_name = "friends"
