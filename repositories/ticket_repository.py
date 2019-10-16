from models.ticket_model import Ticket
from models.comment_model import Comment

class TicketRepostory():

    def get_ticket(self, ticketId):
        return Ticket.select() \
                     .where(Ticket.id == ticketId) \
                     .first()
    
    def get_tickets(self):
        return Ticket.select() \
                     .execute()
    
    def get_product_tickets(self, productId):
        return Ticket.select(Ticket.id, \
                             Ticket.name, \
                             Ticket.creation_date) \
                     .execute()
    
    def get_created_tickets(self, userId):
        return Ticket.select() \
                     .where(Ticket.author_id == userId) \
                     .execute() \

    def get_commented_tickets(self, userId):
        return Ticket.select() \
                     .join(Comment) \
                     .where(Comment.author_id == userId) \
                     .execute()
