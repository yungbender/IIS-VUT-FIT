from models.client_model import UserModel
from flask_login import UserMixin

class User(UserModel, UserMixin):
    
    """ Set table in database for user. (peewee)"""
    class Meta:
        table_name = "client"
    
    """ Method for flask-login to authenticate user ID from cookie. """
    def get_id(self):
        return self.clientname