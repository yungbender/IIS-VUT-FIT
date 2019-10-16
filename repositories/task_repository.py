from models.task_model import Task
from models.user import User
from models.product_model import Product

class TaskRepository():

    def get_task(self, taskId):
        return Task.select()
                   .where(Task.id == taskId)
                   .first()

    def get_tasks(self):
        return Task.select()
                   .execute()

    def get_user_tasks(self, userId):
        return Task.select()
                   .where(Task.worker_id == userId)
                   .execute()
    
    def get_tasks_by(self, userId):
        return Task.select()
                   .where(Task.creator_id == userId)
                   .execute()
    
    def get_product_tasks(self, product):
        return Task.select()
                   .join(User, on=(User.clientname == Task.creator_id))
                   .join(Product, on=(User.clientname == Product.manager_id))
                   .where(Product.name == product)
                   .execute()                   
