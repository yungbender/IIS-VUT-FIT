from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

DASHBOARD_API = Blueprint("create_ticket", __name__)

@DASHBOARD_API.route("/create_ticket", methods=["GET", "POST"])
def index():
    user = current_user
    return render_template("create_ticket.html", user=user, search_image="/Static/search.png")