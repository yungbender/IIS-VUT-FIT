import peewee as pw
from models.base_model import BaseModel

class Task_State(BaseModel):
    id = pw.AutoField(primary_key=True)
    state = pw.CharField(null=False)
