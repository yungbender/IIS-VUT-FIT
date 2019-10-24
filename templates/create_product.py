from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
import wtforms.validators as Validators

class ProductForm(FlaskForm):
    name = StringField("Name", [Validators.input_required()], render_kw={"placeholder": "  Product name"})
    description = StringField("Description", [Validators.input_required()], render_kw={"placeholder": "  Product description"})
    completion_date = StringField("Completion date", [Validators.input_required()], render_kw={"placeholder": "  Product completion date"})
    version = StringField("Version", [Validators.input_required()], render_kw={"placeholder": "  Product version"})
