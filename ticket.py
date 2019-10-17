from flask import Blueprint, render_template
from models.ticket_model import Ticket

TICKET_API = Blueprint("ticket", __name__)

@TICKET_API.route("/ticket/<id>")
def ticket(id):
    if ticket:
        return render_template("ticket.html", ticket=ticket)
    else:
        return 401
