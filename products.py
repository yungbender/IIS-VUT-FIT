from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

PRODUCTS_API = Blueprint("products", __name__)

@PRODUCTS_API.route("/products", methods=["GET", "POST"])
def show_products():
    user = current_user
    return render_template("products.html", user=user, search_image="/Static/search.png")

@PRODUCTS_API.route("/products/new", methods=["GET", "POST"])
def create_products():
    user = current_user
    ProductForm = ProductForm()
    if ProductForm.validate_on_submit():
        product = ProductRepository().create_product()
        return redirect(url_for("products.show_products"))
    return render_template("create_product.html", user=user, search_image="/Static/search.png")