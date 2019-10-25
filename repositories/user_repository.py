from models.user import User
from models.position_model import Position
from models.developer_product_model import DeveloperProduct
from models.product_model import Product

class UserRepository():

    def get_user(self, username):
        return User.select() \
                   .where(User.clientname == username) \
                   .first()
    
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

    def get_product_developers(self, productId):
        return User.select() \
                   .join(DeveloperProduct) \
                   .join(Product) \
                   .where(Product.name == productId) \
                   .execute()

    def register_user(self, username, mail, password):
        User.create(clientname=username, mail=mail, password=password)
    
    def check_user(self, userId):
        return User.select() \
                   .where(User.clientname == userId) \
                   .exists()
