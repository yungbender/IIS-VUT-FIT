import peewee as pw
from basemodel import BaseModel
from clientmodel import Client

class Product(BaseModel):
    name = pw.CharField(primary_key=True)
    description = pw.TextField(null=True)
    image = pw.CharField(default="default")
    creation_date = pw.DateField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    completion_date = pw.DateField(null=True)
    version = pw.CharField(null=True)
    manager_id = pw.ForeignKeyField(Client, backref="product_managed")
