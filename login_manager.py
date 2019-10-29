from repositories.user_repository import UserRepository
from models.user import User
from flask import abort
from flask_login import LoginManager, current_user

LOGIN_MANAGER = LoginManager()
USER_REPOSITORY = UserRepository()
HTTP_NOT_FOUND = 404

@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return USER_REPOSITORY.get_user_username(user_id)
