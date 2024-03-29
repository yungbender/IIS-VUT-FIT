from flask_wtf import FlaskForm
from wtforms import StringField
import wtforms.validators as Validators

class SearchProductForm(FlaskForm):
    product = StringField("Product", render_kw={"placeholder": "Enter product name"}, id="search-bar")