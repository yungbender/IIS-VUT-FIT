from models.user import User

class UserRepository():

    def get_user(self, username):
        return User.select() \
                   .where(User.clientname == username) \
                   .first()
