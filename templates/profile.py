from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField
import wtforms.validators as Validators
from repositories.user_repository import UserRepository

USER_REPO = UserRepository()

class EditProfileForm(FlaskForm):
    mail = StringField("Mail", [Validators.input_required()], render_kw={"placholder": "Your email"}, id="mail")
    name = StringField("Name", render_kw={"placeholder": "Your name"}, id="name")
    surname = StringField("Surname", render_kw={"placeholder": "Your surname"}, id="surname")
    image = FileField("Image", render_kw={"placeholder": "Your profile picture"}, id="image")
    position = SelectField("Position choice", choices=[(position.id, position.position) for position in USER_REPO.get_positions()], coerce=int)
