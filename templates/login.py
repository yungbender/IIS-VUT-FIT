from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
import wtforms.validators as Validators

class LoginForm(FlaskForm):
    username = StringField("Username", [Validators.input_required()], render_kw={"placeholder": "Your username"})
    password = PasswordField("Password", [Validators.input_required()], render_kw={"placeholder": "Your password"})
