from models.user import User
from models.position_model import Position
from models.developer_product_model import DeveloperProduct
from models.product_model import Product

class UserRepository():

    def get_user_username(self, userId):
        return User.select() \
                   .where(User.clientname == userId) \
                   .first()

    def get_user(self, userId):
        return User.select() \
                   .where(User.id == userId) \
                   .first()
    
    def get_users(self, userId):
        return User.select() \
                    .where(User.id != userId) \
                    .execute()

    def get_manager_username(self, username):
        return User.select() \
                   .join(Position) \
                   .where((Position.position == "manager") & (User.clientname == username)) \
                   .first()

    def search_managers(self, managerPattern):
        return User.select() \
                   .join(Position) \
                   .where((Position.position == "manager") & (User.clientname.contains(managerPattern))) \
                   .execute()

    def get_developer_username(self, username):
        return User.select() \
                   .join(Position) \
                   .where((Position.position == "developer") & (User.clientname == username)) \
                   .first()

    def get_product_developers(self, productId):
        return User.select() \
                   .join(DeveloperProduct) \
                   .join(Product) \
                   .where(Product.id == productId) \
                   .execute()

    def register_user(self, username, mail, password):
        User.create(clientname=username, mail=mail, password=password)
    
    def check_user(self, userId):
        return User.select() \
                   .where(User.id == userId) \
                   .exists()
    
    def check_user_username(self, username):
        return User.select() \
                   .where(User.clientname == username) \
                   .exists()

    def search_user(self, pattern, position):
        return User.select() \
                   .join(Position) \
                   .where((Position.id == position) & (User.clientname.contains(pattern))) \
                   .execute()
    
    def get_positions(self):
        return Position.select() \
                       .execute()

    def update_user(self, userId, mail, name, surname, positionId, image=None):
        user = User()
        user.id = userId
        user.mail = mail
        user.name = name
        user.surname = surname
        if image:
            user.image = image
        user.position_id = positionId
        rows = user.save()
        return True if rows > 0 else False
