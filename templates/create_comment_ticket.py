from flask_wtf import FlaskForm
from wtforms import TextField, FileField
import wtforms.validators as Validators

class CreateCommentForm(FlaskForm):
    content = TextField("Comment", [Validators.input_required()], render_kw={"placeholder": "Add new comment"})
    image = FileField(id="choose-image", render_kw={"placeholder": ""})
