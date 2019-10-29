from flask_wtf import FlaskForm
from wtforms import StringField
import wtforms.validators as Validators 

class SearchManagerForm(FlaskForm):
    manager = StringField("Manager", [Validators.input_required()], render_kw={"placeholder": "Search for manager..."}, id="search-manager-bar-input")
