import peewee
import os
from peewee import Model

DB_NAME = os.getenv("DATABASE_NAME", "iis-database")
DB_USER = os.getenv("DATABASE_USER", "iis_webapp")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "iis_passwd")
DB_HOST = os.getenv("DATABASE_HOST", "localhost")

DATABASE = peewee.PostgresqlDatabase(DB_NAME, user=DB_USER, 
                                     password=DB_PASSWORD,
                                     host=DB_HOST, autorollback=True)

# Base model for peewee model mapping
# If you wanna create new model to map from DB, inherit from this
class BaseModel(Model):
    class Meta():
        database = DATABASE
