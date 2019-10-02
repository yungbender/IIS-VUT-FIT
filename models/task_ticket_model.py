import peewee as pw
from models.base_model import BaseModel

from models.task_model import Task
from models.ticket_model import Ticket

class TaskTicket(BaseModel):
    task_id = pw.ForeignKeyField(Task, backref="task_ticket")
    ticket_id = pw.ForeignKeyField(Ticket, backref="ticket_task")
