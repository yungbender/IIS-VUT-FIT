import peewee as pw
from basemodel import BaseModel

class User(BaseModel):
    name = pw.CharField()