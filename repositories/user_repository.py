from models.user import User

class UserRepository():

    def get_user(self, username):
        return User.select() \
                   .where(User.clientname == username) \
                   .first()
    
    def register_user(self, username, mail, password):
        User.create(clientname=username, mail=mail, password=password)