from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user, current_user

LOGOUT_API = Blueprint("logout", __name__)

@LOGOUT_API.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("mainpage.index"))
