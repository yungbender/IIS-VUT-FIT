import peewee as pw
from basemodel import BaseModel
from ticketmodel import Ticket
from clientmodel import Client

class Comment(BaseModel):
    id = pw.AutoField(primary_key=True)
    content = pw.TextField(null=False)
    image = pw.CharField(null=True)
    ticket_id = pw.ForeignKeyField(Ticket, backref="comment_to_ticket")
    author_id = pw.ForeignKeyField(Client, backref="comment_from_author")
