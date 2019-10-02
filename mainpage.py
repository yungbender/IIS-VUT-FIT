from flask import Blueprint, render_template
from flask_login import login_required, current_user

MAINPAGE_API = Blueprint("mainpage", __name__)

@MAINPAGE_API.route("/")
@login_required
def index():
    return render_template("mainpage.html", user=current_user)
