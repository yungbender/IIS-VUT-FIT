from flask import Blueprint, render_template
from flask_login import login_required, current_user
from repositories.ticket_repository import TicketRepository
from repositories.task_repository import TaskRepository
from utilities import format_date, make_thumbnail
import os

DASHBOARD_API = Blueprint("dashboard", __name__)
TICKET_REPO = TicketRepository()
TASK_REPO =  TaskRepository()

CUSTOMER = 0
TICKET_THUMBNAIL_MAX_LENGTH = 15
PRODUCT_THUMBNAIL_MAX_LENGTH = 10
AUTHOR_THUMBNAIL_MAX_LENGTH = 7

@DASHBOARD_API.route("/dashboard", methods=["GET"])
@login_required
def index():
    lastMade = TICKET_REPO.get_created_tickets(current_user.id)
    for ticket in lastMade:
        ticket.name = make_thumbnail(ticket.name, TICKET_THUMBNAIL_MAX_LENGTH)
        ticket.author_id.username = make_thumbnail(ticket.author_id.clientname, AUTHOR_THUMBNAIL_MAX_LENGTH)
        ticket.product_id.name = make_thumbnail(ticket.product_id.name, PRODUCT_THUMBNAIL_MAX_LENGTH)
        ticket.creation_date = format_date(ticket)

    lastCommented = TICKET_REPO.get_commented_tickets(current_user.id)
    for ticket in lastCommented:
        ticket.name = make_thumbnail(ticket.name, TICKET_THUMBNAIL_MAX_LENGTH)
        ticket.author_id.username = make_thumbnail(ticket.author_id.clientname, AUTHOR_THUMBNAIL_MAX_LENGTH)
        ticket.product_id.name = make_thumbnail(ticket.product_id.name, PRODUCT_THUMBNAIL_MAX_LENGTH)
        ticket.creation_date = format_date(ticket)
    if current_user.position_id.id > CUSTOMER:
        assignedTasks = TASK_REPO.get_user_tasks_open(current_user.id)
        return render_template("dashboard.html", user=current_user, assignedTasks=assignedTasks, madeTickets=lastMade, commentedTickets=lastCommented, search_image="/Static/search.png")   
    
    return render_template("dashboard.html", user=current_user, madeTickets=lastMade, commentedTickets=lastCommented, search_image="/Static/search.png")