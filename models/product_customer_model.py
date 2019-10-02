import peewee as pw
from models.base_model import BaseModel
from models.product_model import Product
from models.client_model import Client

class Product_Customer(BaseModel):
    customer_id = pw.ForeignKeyField(Client, backref="customer_product")
    product_id = pw.ForeignKeyField(Product, backref="product_customer")
