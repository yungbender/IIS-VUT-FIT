from flask import Blueprint, request, redirect, render_template
from flask_login import current_user
from repositories.ticket_repository import TicketRepository
from utilities import format_date, make_thumbnail

SEARCH_API = Blueprint("search", __name__)
TICKET_REPO = TicketRepository()

THUMBNAIL_LENGTH = 20

@SEARCH_API.route("/search", methods=["GET"])
def base_search():
    query = request.args.get("query")
    tickets = TICKET_REPO.search_ticket(query)

    for ticket in tickets:
        format_date(ticket)
        ticket.name = make_thumbnail(ticket.name, THUMBNAIL_LENGTH)

    if tickets == True:
        return redirect(f"/tickets/{query}")
    else:
        return render_template("search.html", user=current_user, tickets=tickets)        
