from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
import wtforms.validators as Validators

class RegisterForm(FlaskForm):
    username = StringField("Username", [Validators.input_required()], render_kw={"placeholder": "  Your username"})
    mail = EmailField("E-mail", [Validators.input_required()], render_kw={"placeholder": "  Your e-mail"})
    password = PasswordField("Password", [Validators.input_required()], render_kw={"placeholder": "  Your password"})
    password_re = PasswordField("Confirm Password", [Validators.input_required(), Validators.equal_to("password", message="Passwords must be equal!")], render_kw={"placeholder": "  Please repeat your password."})
