import peewee as pw
from models.base_model import BaseModel

class UserModel(BaseModel):
    clientname = pw.CharField(null=False, primary_key=True)
    mail = pw.CharField(null=False)
    password = pw.CharField(null=False)
    name = pw.CharField(null=True)
    surname = pw.CharField(null=True)
    birth = pw.DateField(null=True)
    image = pw.CharField(null=False, default="default")
    position = pw.CharField(null=False, default="customer")
    work_time = pw.IntegerField(null=True, default=0)
