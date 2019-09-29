import peewee as pw
from basemodel import BaseModel
from productmodel import Product
from clientmodel import Client

class Product_Customer(BaseModel):
    customer_id = pw.ForeignKeyField(Client, backref="customer_product")
    product_id = pw.ForeignKeyField(Product, backref="product_customer")
