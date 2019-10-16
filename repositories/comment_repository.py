from models.comment_model import Comment
from models.ticket_model import Ticket

class CommentRepository:

    def get_ticket_comments(self, ticketId):
        return Comment.select() \
                      .join(Ticket)
                      .where(Ticket.id == ticketId)
                      .execute()
    