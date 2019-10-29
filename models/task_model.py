import peewee as pw
from models.base_model import BaseModel
from models.client_model import Client
from models.ticket_model import Ticket
from models.task_state_model import Task_State

DEFAULT_STATE = Task_State()
DEFAULT_STATE.id = 1

class Task(BaseModel):
    id = pw.AutoField(primary_key=True)
    title = pw.CharField(null=False)
    description = pw.TextField(null=True)
    completion_date = pw.CharField(null=True)
    creation_date = pw.DateField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    state = pw.ForeignKeyField(Task_State, default=DEFAULT_STATE)
    worker_id = pw.ForeignKeyField(Client, backref="worked_task")
    creator_id = pw.ForeignKeyField(Client, backref="created_task")
