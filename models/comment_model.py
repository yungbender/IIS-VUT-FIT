import peewee as pw
from models.base_model import BaseModel
from models.ticket_model import Ticket
from models.client_model import Client
from models.task_model import Task

class Comment(BaseModel):
    id = pw.AutoField(primary_key=True)
    content = pw.TextField(null=False)
    image = pw.CharField(null=True)
    creation_date = pw.DateField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    answer = pw.BooleanField(null=False, default=False)
    ticket_id = pw.ForeignKeyField(Ticket, backref="comment_to_ticket")
    author_id = pw.ForeignKeyField(Client, backref="comment_from_author")
    task_id = pw.ForeignKeyField(Task, backref="comment_to_task")
