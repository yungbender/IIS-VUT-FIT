from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, FileField
import wtforms.validators as Validators

class ProductForm(FlaskForm):
    name = StringField("Name", [Validators.input_required()], render_kw={"placeholder": "  Product name"})
    description = TextAreaField("Description", [Validators.input_required()], render_kw={"placeholder": "  Product description"})
    completion_date = StringField("Completion date", [Validators.input_required()], render_kw={"placeholder": "  Product completion date"})
    version = StringField("Version", [Validators.input_required()], render_kw={"placeholder": "  Product version"})
    image = FileField(render_kw={"placeholder": ""})
    manager_id = StringField("Manager ID", [Validators.input_required()], render_kw={"placeholder": "  Responsible manager"})