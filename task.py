from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required
from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository
from repositories.ticket_repository import TicketRepository
from templates.create_task import CreateTaskForm

TASK_API = Blueprint("task", __name__)
TASK_REPO = TaskRepository()
TICKET_REPO = TicketRepository()
USER_REPO = UserRepository()
HTTP_UNAUTHORIZED = 401
HTTP_NOT_FOUND = 404
MANAGER = 2

@TASK_API.route("/tasks")
@login_required
def get_tasks():
    assignedTasks = TASK_REPO.get_user_tasks(current_user.id)
    createdTasks = TASK_REPO.get_tasks_by(current_user.id)
    return render_template("tasks.html", user=current_user, 
                           assignedTasks=assignedTasks, createdTasks=createdTasks)

@TASK_API.route("/tasks/<int:taskId>", methods=["GET", "POST"])
@login_required
def get_specific_task(taskId):
    task = TASK_REPO.get_task(taskId)
    if not task:
        abort(HTTP_NOT_FOUND)
    # Given task is not maintained or fullfilled by requesting user
    taskRequester = current_user.id
    if taskRequester != task.creator_id.id and taskRequester != task.worker_id.id:
        abort(HTTP_UNAUTHORIZED)

    taskForm = CreateTaskForm()

    if taskForm.validate_on_submit():
        # User wants to edit existing ticket
        ticketId = taskForm.ticket.data
        taskTitle = taskForm.title.data
        taskDesc = taskForm.description.data
        taskDate = taskForm.completion_date.data 
        taskState = taskForm.state.data
        taskWorker = taskForm.worker.data
        developer = USER_REPO.get_developer_username(taskWorker)
        if developer:
            success = TASK_REPO.update_task(taskId, taskTitle, taskDesc, taskDate, taskState, developer.id)
            if success:
                return redirect(url_for("dashboard.index"))

    # User wants to see the ticket
    relatedTickets = TICKET_REPO.get_task_tickets(taskId)

    taskForm.title.data = task.title
    taskForm.description.data = task.description
    taskForm.completion_date.data = task.completion_date
    taskForm.state.data = task.state_id.id 
    taskForm.worker.data = task.worker_id.clientname

    return render_template("task.html", user=current_user, taskId=taskId, taskForm=taskForm, relatedTickets=relatedTickets)

@TASK_API.route("/tasks/new", methods=["GET", "POST"])
def create_task():
    if current_user.position_id.id < MANAGER:
        abort(HTTP_UNAUTHORIZED)

    ticketIdPrefill = request.args.get("ticket")
    taskForm = CreateTaskForm()
    taskForm.ticket.data = ticketIdPrefill

    if taskForm.validate_on_submit():
        ticketId = taskForm.ticket.data
        taskCreator = current_user.id
        taskTitle = taskForm.title.data
        taskDesc = taskForm.description.data
        taskDate = taskForm.completion_date.data 
        taskState = taskForm.state.data
        taskWorker = taskForm.worker.data
        developer = USER_REPO.get_developer_username(taskWorker)
        if developer:
            if ticketId is None:
                TASK_REPO.create_task(taskTitle, taskDesc, taskDate, developer.id, taskCreator, taskState, ticketId)
                return redirect(url_for("dashboard.index"))
            else:
                isCorrect = True
                try:
                    ticketId = int(taskForm.ticket.data)
                except ValueError:
                    isCorrect = False

                if isCorrect:
                    ticket = TICKET_REPO.get_ticket(ticketId)
                    if ticket:
                        TASK_REPO.create_task(taskTitle, taskDesc, taskDate, developer.id, taskCreator, taskState, ticketId)
                        return redirect(url_for("dashboard.index"))

    return render_template("create_task.html", user=current_user, taskForm=taskForm)