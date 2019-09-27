from flask import Blueprint, render_template

MAINPAGE_API = Blueprint("mainpage", __name__)

@MAINPAGE_API.route("/")
def index():
    return render_template("mainpage.html")