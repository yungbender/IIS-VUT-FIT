from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

MAINPAGE_API = Blueprint("mainpage", __name__)

@MAINPAGE_API.route("/")
def index():
    user = current_user
    return render_template("mainpage.html", user=user, search_image="/Static/search.png")

@MAINPAGE_API.route("/error")
def error():
    user = current_user
    return render_template("error.html", user=user)

@MAINPAGE_API.route("/404")
def e404():
    user = current_user
    return render_template("404.html", user=user)

@MAINPAGE_API.route("/403")
def e403():
    user = current_user
    return render_template("403.html", user=user)

@MAINPAGE_API.route("/400")
def e400():
    user = current_user
    return render_template("400.html", user=user)
