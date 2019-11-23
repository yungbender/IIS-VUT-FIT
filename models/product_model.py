import peewee as pw
from models.base_model import BaseModel
from models.client_model import Client

class Product(BaseModel):
    id = pw.AutoField(primary_key=True)
    name = pw.CharField(null=False)
    description = pw.TextField(null=True)
    image = pw.CharField(default="2.jpg")
    creation_date = pw.DateField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    completion_date = pw.DateField(null=True)
    version = pw.CharField(null=True)
    creator_id = pw.ForeignKeyField(Client, backref="product_creator")
    manager_id = pw.ForeignKeyField(Client, backref="product_managed")
