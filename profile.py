from flask import Blueprint, render_template
from models.user import User

PROFILE_API = Blueprint("profile", __name__)

@PROFILE_API.route("/profile/<username>")
def profile(username):
    user = User().select().where(User.clientname == username).first()
    if user:
        return render_template("profile.html", user=user)
    else:
        return 401
