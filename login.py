from flask import render_template, Blueprint, redirect, url_for
from templates.login import LoginForm

LOGIN_API = Blueprint("login", __name__)

@LOGIN_API.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        return redirect(url_for("mainpage.index"))
    return render_template("login.html", form=loginForm)