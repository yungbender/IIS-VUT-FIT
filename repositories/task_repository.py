from models.task_model import Task
from models.user import User
from models.product_model import Product
from models.ticket_model import Ticket
from models.task_ticket_model import Task_Ticket
from models.task_state_model import Task_State

class TaskRepository():

    def get_task(self, taskId):
        return Task.select() \
                   .where(Task.id == taskId) \
                   .first()

    def get_tasks(self):
        return Task.select() \
                   .execute()

    def get_user_tasks(self, userId):
        return Task.select() \
                   .where(Task.worker_id == userId) \
                   .execute()
    
    def get_tasks_by(self, userId):
        return Task.select() \
                   .where(Task.creator_id == userId) \
                   .execute()
    
    def get_product_tasks(self, product):
        return Task.select() \
                   .join(User, on=(User.clientname == Task.creator_id)) \
                   .join(Product, on=(User.clientname == Product.manager_id)) \
                   .where(Product.name == product) \
                   .execute()
    
    def get_ticket_tasks(self, ticketId):
        return Task.select() \
                   .join(TaskTicket) \
                   .join(Ticket) \
                   .where(Ticket.id == ticketId) \
                   .execute()

    def create_task(self, title, description, completionDate, workerId, creatorId, state, basedOn):
        print(print(basedOn))
        newTask = Task.create(title=title, description=description, 
                    completion_date=completionDate, 
                    state=state, worker_id=workerId, creator_id=creatorId,
                    based_on=basedOn)
        
        if basedOn:
            TaskTicket.create(task_id=newTask.id, ticket_id=basedOn)

    def update_task_state(self, taskId, state):
        task = Task()
        task.id = taskId
        task.state = state
        task.save()

    def get_task_states(self):
        return Task_State.select() \
                        .execute()
