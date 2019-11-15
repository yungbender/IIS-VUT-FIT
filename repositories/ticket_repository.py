from models.ticket_model import Ticket
from models.comment_model import Comment
from models.product_model import Product
from models.task_ticket_model import Task_Ticket

class TicketRepository():

    def get_ticket(self, ticketId):
        return Ticket.select() \
                     .where(Ticket.id == ticketId) \
                     .first()
    
    def get_tickets(self):
        return Ticket.select() \
                     .execute()
    
    def get_product_tickets(self, productId):
        return Ticket.select() \
                     .join(Product) \
                     .where(Product.id == productId) \
                     .execute()
    
    def get_created_tickets(self, userId):
        return Ticket.select() \
                     .where(Ticket.author_id == userId) \
                     .order_by(Ticket.creation_date.desc()) \
                     .execute()

    def get_commented_tickets(self, userId):
        return Ticket.select() \
                     .distinct(Ticket.id) \
                     .join(Comment) \
                     .where(Comment.author_id == userId) \
                     .order_by(Comment.creation_date.desc()) \
                     .execute()

    def get_task_tickets(self, taskId):
        return Ticket.select() \
                     .join(Task_Ticket) \
                     .where(Task_Ticket.task_id == taskId) \
                     .execute()

    def create_ticket(self, name, description, image, authorId, productId, state=0):
        Ticket.create(name=name, description=description, state=state, author_id=authorId, product_id=productId)
    
    def update_ticket_state(self, ticketId, state):
        ticket = Ticket()
        ticket.id = ticketId
        ticket.state = state
        ticket.save()

    def search_ticket(self, pattern):
        try:
            id = int(pattern)
            if Ticket.select().where(Ticket.id == id).exists():
                return True
        except TypeError:
            tickets = Ticket.select().where(Ticket.name.contains(pattern)).execute()
            return tickets

