import peewee as pw
from models.base_model import BaseModel
from models.user import User
from models.product_model import Product

class DeveloperProduct(BaseModel):
    developer_id = pw.ForeignKeyField(User, null=False)
    product_id = pw.ForeignKeyField(Product, null=False)
