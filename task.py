from flask import Blueprint
from flask_login import current_user
from repositories.task_repository import TaskRepository

TASK_API = Blueprint("task", __name__)
TASK_REPO = TaskRepository()

@TASK_API.route("/task")
def tasks():
    tasks = TASK_REPO.get_tasks()

@TASK_API.route("/tasks/<int:id>")
def task(id):
    task = TASK_REPO.get_task(id)
