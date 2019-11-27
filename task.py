from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import current_user, login_required
from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository
from repositories.ticket_repository import TicketRepository
from repositories.comment_repository import CommentRepository
from templates.create_task import CreateTaskForm
from templates.create_comment_ticket import CreateCommentForm
from upload_handler import handle_image, InvalidFile
from utilities import make_thumbnail
from peewee import PeeweeException

TASK_API = Blueprint("task", __name__)
TASK_REPO = TaskRepository()
TICKET_REPO = TicketRepository()
USER_REPO = UserRepository()
COMMENT_REPO = CommentRepository()
HTTP_UNAUTHORIZED = 401
HTTP_NOT_FOUND = 404
MANAGER = 2
TASK_MAX_THUMBNAIL_LENGTH = 23

@TASK_API.route("/tasks")
@login_required
def get_tasks():
    assignedTasks = TASK_REPO.get_user_tasks(current_user.id)
    for task in assignedTasks:
        task.title = make_thumbnail(task.title, TASK_MAX_THUMBNAIL_LENGTH)
    createdTasks = TASK_REPO.get_tasks_by(current_user.id)
    for task in createdTasks:
        task.title = make_thumbnail(task.title, TASK_MAX_THUMBNAIL_LENGTH)
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
    commentForm = CreateCommentForm()

    if taskForm.validate_on_submit():
        # User wants to edit existing ticket
        ticketId = taskForm.ticket.data
        taskTitle = taskForm.title.data
        taskDesc = taskForm.description.data
        taskDate = taskForm.completion_date.data 
        taskState = taskForm.state.data
        taskWorker = taskForm.worker.data
        asignee = USER_REPO.get_user_username(taskWorker)
        if asignee:
            try:
                success = TASK_REPO.update_task(taskId, taskTitle, taskDesc, taskDate, taskState, asignee.id)
            except PeeweeException:
                flash("Cannot save! Check length of elements!", "task")
                success = False
            if success:
                return redirect(url_for("dashboard.index"))
        else:
            flash("Asignee does not exist!", "task")
    elif commentForm.validate_on_submit():
        comment = commentForm.content.data
        try:
            image = handle_image(commentForm.image)
        except InvalidFile:
            return flash("Invalid file uploaded!", "task")

        try:
            COMMENT_REPO.create_task_comment(comment, image, taskId, current_user.id)
        except PeeweeException:
            flash("Cannot save! Check length of elements!", "task")

    # Get related tickets to the task
    relatedTickets = TICKET_REPO.get_task_tickets(taskId)
    taskComments = COMMENT_REPO.get_task_comments(taskId)

    taskForm.title.data = task.title
    taskForm.description.data = task.description
    taskForm.completion_date.data = task.completion_date
    taskForm.state.data = task.state_id.id 
    taskForm.worker.data = task.worker_id.clientname

    return render_template("task.html", user=current_user, taskId=taskId, taskForm=taskForm, relatedTickets=relatedTickets, comments=taskComments, commentForm=commentForm)

@TASK_API.route("/tasks/new", methods=["GET", "POST"])
def create_task():
    if current_user.position_id.id < MANAGER:
        abort(HTTP_UNAUTHORIZED)

    taskForm = CreateTaskForm()

    if taskForm.validate_on_submit():
        ticketId = taskForm.ticket.data
        taskCreator = current_user.id
        taskTitle = taskForm.title.data
        taskDesc = taskForm.description.data
        taskDate = taskForm.completion_date.data 
        taskState = taskForm.state.data
        taskWorker = taskForm.worker.data
        asignee = USER_REPO.get_user_username(taskWorker)
        if asignee:
            if ticketId is None:
                try:
                    success = TASK_REPO.create_task(taskTitle, taskDesc, taskDate, asignee.id, taskCreator, taskState, ticketId)
                except PeeweeException:
                    success = False
                    flash("Cannot save! Check length of elements!", "task")
                if success:
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
                        try:
                            TASK_REPO.create_task(taskTitle, taskDesc, taskDate, asignee.id, taskCreator, taskState, ticketId)
                        except PeeweeException:
                            flash("Cannot save! Check length of elements!", "task")
                            return render_template("create_task.html", user=current_user, taskForm=taskForm)

                        return redirect(url_for("dashboard.index"))

                flash("Ticket does not exists!", "task")
        else:
            flash("Asignee does not exists!", "task")

    return render_template("create_task.html", user=current_user, taskForm=taskForm)