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
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for("mainpage.index"))

    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        user = USER_REPOSITORY.get_user(registerForm.username.data)
        if not user:
            pwd_encrypted = sha512((registerForm.password.data + SECRET_KEY).encode("utf-8")).hexdigest()
            USER_REPOSITORY.register_user(registerForm.username.data, registerForm.mail.data, pwd_encrypted)
            #login_user(user)
            return redirect(url_for("mainpage.index"))
    print(registerForm.errors)  
    return render_template("register.html", form=registerForm)