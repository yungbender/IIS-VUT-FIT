from flask import Blueprint, render_template
from models.user import User
from repositories.user_repository import UserRepository

PROFILE_API = Blueprint("profile", __name__)
USER_REPO = UserRepository()

@PROFILE_API.route("/profile/<username>")
def profile(username):
    user = USER_REPO.get_user(username) 
    if user:
        return render_template("profile.html", user=user)
    else:
        return 401
