from flask_wtf import FlaskForm
from wtforms import StringField, FileField
import wtforms.validators as Validators

class CreateTicketForm(FlaskForm):
    title = StringField("Title", [Validators.input_required()], render_kw={"placeholder": "Title"})
    description = StringField("Description", [Validators.input_required()], render_kw={"placeholder": "Detailed description"})
    image = FileField("Image", render_kw={"placeholder": "Add ticket image to describe"})
