from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

DASHBOARD_API = Blueprint("dashboard", __name__)

@DASHBOARD_API.route("/dashboard", methods=["GET", "POST"])
def index():
    user = current_user
    print(type(user.position_id))
    return render_template("dashboard.html", user=user, search_image="/Static/search.png")