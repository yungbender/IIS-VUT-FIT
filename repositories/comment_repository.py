from models.comment_model import Comment
from models.ticket_model import Ticket
from models.task_model import Task

class CommentRepository:

    def get_ticket_comments(self, ticketId):
        return Comment.select() \
                      .join(Ticket) \
                      .where(Ticket.id == ticketId) \
                      .order_by(Comment.creation_date.asc()) \
                      .execute()
    
    def get_task_comments(self, taskId):
        return Comment.select() \
                      .join(Task) \
                      .where(Task.id == taskId) \
                      .order_by(Task.creation_date.asc()) \
                      .execute()
    
    def get_comment(self, commentId):
        return Comment.select() \
                      .where(Comment.id == commentId) \
                      .first()

    def create_ticket_comment(self, content, image, ticketId, authorId):
        Comment.create(content=content, image=image, ticket_id=ticketId, author_id=authorId)
    
    def create_task_comment(self, content, image, taskId, authorId):
        Comment.create(content=content, image=image, task_id=taskId, author_id=authorId)
