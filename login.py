from flask import render_template, Blueprint, redirect, url_for, flash, session
from templates.login import LoginForm
from templates.register import RegisterForm

from models.user import User
from flask_login import login_user, current_user
from repositories.user_repository import UserRepository

from hashlib import sha512

LOGIN_API = Blueprint("login", __name__)
USER_REPOSITORY = UserRepository()

SECRET_KEY = "30c2eaa65b970b48317e4120efc4a7f8"

@LOGIN_API.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = USER_REPOSITORY.get_user_username(loginForm.username.data)
        if user:

            pwd_encrypted = sha512((loginForm.password.data + SECRET_KEY).encode("utf-8")).hexdigest()
            if user.password == pwd_encrypted:
                session.permanent = True
                login_user(user)
                return redirect(url_for("dashboard.index"))
        
        flash("Incorrect username or password!", "creditials")

    return render_template("login.html", form=loginForm, user=current_user)
