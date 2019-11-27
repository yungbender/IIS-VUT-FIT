from models.task_model import Task
from models.user import User
from models.product_model import Product
from models.ticket_model import Ticket
from models.task_ticket_model import Task_Ticket
from models.task_state_model import Task_State

TASK_DONE = 4

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
        newTask = Task.create(title=title, description=description, 
                    completion_date=completionDate, 
                    state=state, worker_id=workerId, creator_id=creatorId)
        
        if basedOn:
            Task_Ticket.create(task_id=newTask.id, ticket_id=basedOn)

        return True

    def update_task(self, taskId, title, description, completionDate, stateId, workerId):
        task = Task()
        task.id = taskId
        task.title = title
        task.description = description
        task.completion_date = completionDate
        task.state_id = stateId
        task.worker_id = workerId
        rows = task.save()
        return True if rows > 0 else False

    def get_task_states(self):
        return Task_State.select() \
                        .execute()

    def get_user_tasks_open(self, userId):
        return Task.select() \
                   .join(Task_State) \
                   .where((Task.worker_id == userId) & (Task_State.id < TASK_DONE)) \
                   .execute()
