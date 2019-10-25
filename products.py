from flask import Blueprint, render_template
from flask_login import login_required, current_user
from repositories.product_repository import ProductRepository
from templates.create_product import ProductForm
import os

PRODUCTS_API = Blueprint("products", __name__)
PRODUCTS_REPO = ProductRepository()

@PRODUCTS_API.route("/products")
def show_products():
    products = PRODUCTS_REPO.get_products()
    return render_template("products.html", user=current_user, search_image="/Static/search.png", products=products)

@PRODUCTS_API.route("/products/new", methods=["GET", "POST"])
def create_products():
    productForm = ProductForm()
    if productForm.validate_on_submit():
        productName = productForm.name.data
        if PRODUCTS_REPO.check_product(productName):
            productDesc = productForm.description.data
            productCompletion = productForm.completion_date.data
            productVer = productForm.version.data
            PRODUCTS_REPO.create_product(productName, productDesc, productCompletion, productVer)

    return render_template("create_product.html", user=current_user, search_image="/Static/search.png", productForm=productForm)