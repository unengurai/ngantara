#!/usr/bin/env python3

import datetime
import peewee

from config import dbconfig
db = dbconfig['sqlite']['db']
database = peewee.SqliteDatabase(db)


class BaseModel(peewee.Model):
    """Base model"""
    class Meta:
        database = database


class KeywordType(BaseModel):
    ktid = peewee.PrimaryKeyField()
    kwtype = peewee.CharField(max_length=128, unique=True)
    app = peewee.CharField(max_length=128)
    note = peewee.CharField(max_length=128)
    

class Keyword(BaseModel):
    kwid = peewee.PrimaryKeyField()
    kw = peewee.CharField(max_length=128, unique=True)
    kwtype = peewee.IntegerField()
    checked = peewee.CharField(max_length=2, default=3)
    cdate = peewee.DateField(default=datetime.date.today)
    
class SearchResult(BaseModel):
    srid = peewee.PrimaryKeyField()
    url = peewee.CharField(max_length=128, unique=True)
    kw = peewee.IntegerField()
    kwtype = peewee.IntegerField()
    cdate = peewee.DateField()


all_model = [KeywordType,Keyword,SearchResult]


def init():
    """utility function to initialize tables and database"""
    database.connect()
    peewee.create_model_tables(all_model, fail_silently=False)
