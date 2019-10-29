from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from templates.create_product import ProductForm
from templates.search_manager import SearchManagerForm
from templates.search_product import SearchProductForm
from upload_handler import handle_image, remove_file
import os

PRODUCT_API = Blueprint("products", __name__)
PRODUCT_REPO = ProductRepository()
USER_REPO = UserRepository()

@PRODUCT_API.route("/products", methods=["GET", "POST"])
def show_products():

    searchForm = SearchProductForm()

    if searchForm:
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
        
        if not PRODUCT_REPO.check_product(productName):
            productDesc = productForm.description.data
            productCompletion = productForm.completion_date.data
            productVer = productForm.version.data
            productManager = productForm.manager_id.data
            if USER_REPO.check_user(productManager):
                productImage = handle_image(productForm.image)
                try:
                    PRODUCT_REPO.create_product(productName, productDesc, productCompletion, productVer, productManager, productImage)
                except Exception:
                    remove_file(productImage)
                return redirect(url_for("dashboard.index"))

    if managerForm.validate_on_submit():
        managerPattern = managerForm.manager.data
    
        managers = USER_REPO.search_managers(managerPattern)
        
        return render_template("create_product.html", user=current_user, \
                               search_image="/Static/search.png", productForm=productForm, \
                               managerForm=managerForm, managers=managers)

    return render_template("create_product.html", user=current_user, \
                           search_image="/Static/search.png", productForm=productForm, \
                           managerForm=managerForm, managers=[])