from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

MAINPAGE_API = Blueprint("mainpage", __name__)

@MAINPAGE_API.route("/")
def index():
    user = current_user
    return render_template("mainpage.html", user=user, search_image="/Static/search.png")
