from repositories.user_repository import UserRepository
from models.user import User
from flask_login import LoginManager, current_user
from flask import redirect, url_for, session
from werkzeug.routing import RequestRedirect

LOGIN_MANAGER = LoginManager()

USER_REPOSITORY = UserRepository()

@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return USER_REPOSITORY.get_user(user_id)

def login_forbidden(target):
    def wrap_up(f):
        def wrap(*args, **kwargs):
            if "user_id" in session:
                raise RequestRedirect(url_for(target))
            return f(*args, **kwargs)
        return wrap
    return wrap_up
