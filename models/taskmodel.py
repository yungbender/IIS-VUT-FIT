import peewee as pw
from basemodel import BaseModel
from clientmodel import Client
from ticketmodel import Ticket

class Task(BaseModel):
    id = pw.AutoField(primary_key=True)
    title = pw.CharField(null=False)
    description = pw.TextField(null=True)
    completion_date = pw.TimestampField(null=True)
    state = pw.SmallIntegerField(null=False, default=0)
    creation_date = pw.TimestampField(null=False, constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    worker_id = pw.ForeignKeyField(Client, backref="worked_task")
    creator_id = pw.ForeignKeyField(Client, backref="created_task")
    based_on = pw.ForeignKeyField(Ticket, backref="Task_based_on_ticket")
