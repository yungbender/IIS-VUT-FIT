import peewee as pw
from models.base_model import BaseModel
from models.client_model import Client

class Product(BaseModel):
    name = pw.CharField(primary_key=True)
    description = pw.TextField(null=True)
    image = pw.CharField(default="2.jpg")
    creation_date = pw.DateField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    completion_date = pw.DateField(null=True)
    version = pw.CharField(null=True)
    manager_id = pw.ForeignKeyField(Client, backref="product_managed")
