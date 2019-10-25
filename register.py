from login import SECRET_KEY

from flask import render_template, Blueprint, redirect, url_for, flash
from templates.login import LoginForm
from templates.register import RegisterForm

from models.user import User
from flask_login import login_user, current_user
from repositories.user_repository import UserRepository

from hashlib import sha512

REGISTER_API = Blueprint("register", __name__)
USER_REPOSITORY = UserRepository()

@REGISTER_API.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("mainpage.index"))

    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        username = registerForm.username.data
        mail = registerForm.mail.data
        if not USER_REPOSITORY.check_user(username):
            pwd_encrypted = sha512((registerForm.password.data + SECRET_KEY).encode("utf-8")).hexdigest()
            USER_REPOSITORY.register_user(username, mail, pwd_encrypted)
            #login_user(user)
            return redirect(url_for("mainpage.index"))
    return render_template("register.html", form=registerForm, user=current_user)