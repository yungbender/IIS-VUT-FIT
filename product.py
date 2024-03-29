from flask import Blueprint, render_template, url_for, redirect, abort, request, flash
from flask_login import login_required, current_user
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from templates.create_product import ProductForm
from templates.search_manager import SearchManagerForm
from templates.search_product import SearchProductForm
from upload_handler import handle_image, remove_file, InvalidFile
from peewee import PeeweeException
import os

PRODUCT_API = Blueprint("products", __name__)
PRODUCT_REPO = ProductRepository()
USER_REPO = UserRepository()
HTTP_NOT_FOUND = 404

@PRODUCT_API.route("/products", methods=["GET", "POST"])
def show_products():

    searchForm = SearchProductForm()

    if searchForm.validate_on_submit():
        productPattern = searchForm.product.data
        products = PRODUCT_REPO.search_product(productPattern)
        return render_template("products.html", user=current_user, search_image="/Static/search.png", products=products, searchForm=searchForm)

    products = PRODUCT_REPO.get_products()
    return render_template("products.html", user=current_user, search_image="/Static/search.png", products=products, searchForm=searchForm)

@PRODUCT_API.route("/products/new", methods=["GET", "POST"])
def create_products():
    productForm = ProductForm()
    managerForm = SearchManagerForm()

    if productForm.validate_on_submit():
        productName = productForm.name.data
        
        if not PRODUCT_REPO.check_product_productname(productName):
            productDesc = productForm.description.data
            productCompletion = productForm.completion_date.data
            productVer = productForm.version.data
            productManager = productForm.manager_id.data
            productManager = USER_REPO.get_manager_username(productManager)
            if productManager:
                try:
                    productImage = handle_image(productForm.image)
                    PRODUCT_REPO.create_product(productName, productDesc, productCompletion, productVer, current_user.id, productManager.id, productImage)
                except (PeeweeException, InvalidFile):
                    flash("Cannot save! Check length of elements!", "product")
                    return render_template("create_product.html", user=current_user, \
                       search_image="/Static/search.png", productForm=productForm, \
                           managerForm=managerForm, managers=[])
                return redirect(url_for("dashboard.index"))
            else:
                flash("Invalid user selected as manager!", "product")
        
        else:
            flash("Product already exists!", "product")

    return render_template("create_product.html", user=current_user, \
                           search_image="/Static/search.png", productForm=productForm, \
                               managerForm=managerForm, managers=[])

@PRODUCT_API.route("/products/<int:productId>")
def get_product(productId):
    product = PRODUCT_REPO.get_product(productId)
    if not product:
        return abort(HTTP_NOT_FOUND)
    return render_template("product.html", user=current_user, product=product)
