import peewee as pw
from models.base_model import BaseModel

class Position(BaseModel):
    id = pw.IntegerField(primary_key=True)
    position = pw.CharField(null=False)
