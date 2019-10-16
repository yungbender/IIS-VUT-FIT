from models.user import User
from models.position_model import Position

class UserRepository():

    def get_user(self, username):
        return User.select() \
                   .where(User.clientname == username) \
                   .first()
    
    def register_user(self, username, mail, password):
        User.create(clientname=username, mail=mail, password=password)
    
    def get_users(self, username):
        return User.select() \
                    .where(User.clientname != username) \
                    .execute()

    def get_managers(self, username):
        return User.select() \
                   .join(Position) \
                   .where(Position.position == "manager" and User.clientname != username) \
                   .execute()

    def get_developers(self, username):
        return User.select() \
                   .join(Position) \
                   .where(Position.position == "developer" and user.clientname != username) \
                   .execute()
