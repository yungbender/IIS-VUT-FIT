import peewee as pw
from models.base_model import BaseModel
from models.product_model import Product
from models.client_model import Client

class Ticket(BaseModel):
    id = pw.AutoField(primary_key=True)
    name = pw.CharField(null=False)
    description = pw.TextField(null=False)
    state = pw.SmallIntegerField(null=False, default=0)
    creation_date = pw.TimestampField(null=False, constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    image = pw.CharField(null=True)
    author_id = pw.ForeignKeyField(Client, backref="ticket_by")
    product_id = pw.ForeignKeyField(Product, backref="ticket_for_product")
