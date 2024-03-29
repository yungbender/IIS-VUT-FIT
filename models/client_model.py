import peewee as pw
from models.base_model import BaseModel
from models.position_model import Position

class Client(BaseModel):
    id = pw.AutoField(primary_key=True)
    clientname = pw.CharField(null=False)
    mail = pw.CharField(null=False)
    password = pw.CharField(null=False)
    name = pw.CharField(null=True)
    surname = pw.CharField(null=True)
    birth = pw.DateField(null=True)
    image = pw.CharField(null=False, default="1.jpg")
    registration_date = pw.DateField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    position_id = pw.ForeignKeyField(Position, null=False, default=0)
    work_time = pw.IntegerField(null=True, default=0)
