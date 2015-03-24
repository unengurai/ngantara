#!/usr/bin/env python3

import datetime
import peewee

from config import dbconfig

##- amun makai sqlite.
#db = dbconfig['sqlite']['db']
#database = peewee.SqliteDatabase(db)

##- amun makai pgsql
db = dbconfig['postgre']['db_name']
db_uname = dbconfig['postgre']['user']
db_passwd =  dbconfig['postgre']['password']
database = peewee.PostgresqlDatabase\
           (db, user=db_uname, password=db_passwd)

class BaseModel(peewee.Model):
    """Base model"""

    class Meta:
        database = database


class KeywordType(BaseModel):
    id = peewee.PrimaryKeyField()
    kwtype = peewee.CharField(max_length=128, unique=True)
    app = peewee.CharField(max_length=128)
    note = peewee.CharField(max_length=128)


class Keyword(BaseModel):
    id = peewee.PrimaryKeyField()
    kw = peewee.CharField(max_length=128, unique=True)
    kwtype_id = peewee.IntegerField()
    ##- checked maksud ni pakai pananda:
    ##  1=luput, 2=haut na alap, 3=hu'an na alap
    checked = peewee.CharField(max_length=2, default=3)
    cdate = peewee.DateField(default=datetime.date.today)


class SearchResult(BaseModel):
    id = peewee.PrimaryKeyField()
    url = peewee.CharField(max_length=128)
    kw_id = peewee.IntegerField()
    cdate = peewee.DateField(default=datetime.date.today)


class AuthKey(BaseModel):
    id = peewee.PrimaryKeyField()
    key = peewee.CharField(max_length=16, unique=True)
    active = peewee.BooleanField()


all_model = [KeywordType, Keyword, SearchResult, AuthKey]


def create_model():
    database.connect()
    peewee.create_model_tables(all_model, fail_silently=False)
