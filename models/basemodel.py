import peewee
from peewee import Model

DATABASE = peewee.PostgresqlDatabase()

# Base model for peewee model mapping
# If you wanna create new model to map from DB, inherit from this
class BaseModel(Model):
    class Meta():
        database = DATABASE
