from flask import Blueprint, request, redirect, render_template
from flask_login import current_user
from repositories.ticket_repository import TicketRepository

SEARCH_API = Blueprint("search", __name__)
TICKET_REPO = TicketRepository()

@SEARCH_API.route("/search", methods=["GET"])
def base_search():
    query = request.args.get("query")
    tickets = TICKET_REPO.search_ticket(query)

    if tickets == True:
        return redirect(f"/tickets/{query}")
    else:
        return render_template("search.html", user=current_user, tickets=tickets)        
