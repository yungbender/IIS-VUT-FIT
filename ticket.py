from flask import Blueprint, render_template, abort, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from models.ticket_model import Ticket
from repositories.ticket_repository import TicketRepository
from repositories.product_repository import ProductRepository
from templates.create_ticket import CreateTicketForm
from templates.search_product import SearchProductForm
from upload_handler import handle_image, InvalidFile, remove_file

TICKET_API = Blueprint("ticket", __name__)
TICKET_REPO = TicketRepository()
PRODUCT_REPO = ProductRepository()
HTTP_NOT_FOUND = 404

@TICKET_API.route("/tickets/<int:productId>/<int:ticketId>")
def product_ticket(productId, ticketId):
    if PRODUCT_REPO.check_product(productId):
        ticket = TICKET_REPO.get_ticket(ticketId)
        if ticket:
            return render_template("ticket.html", ticket=ticket, user=current_user)
    return abort(HTTP_NOT_FOUND)

@TICKET_API.route("/tickets/<int:productId>")
def product_tickets(productId):
    if PRODUCT_REPO.check_product(productId):
        tickets = TICKET_REPO.get_product_tickets(productId)
        return render_template("tickets.html", tickets=tickets, user=current_user, productId=productId)
    return abort(HTTP_NOT_FOUND)

@TICKET_API.route("/tickets/new", methods=["GET", "POST"])
@login_required
def create_ticket_products():
    # User wants to create ticket, but firstly he needs to search for 
    # product to which the ticket will be commited
    productForm = SearchProductForm()
    # If user searched for product
    if productForm.validate_on_submit():
        productPattern = productForm.product.data
        searchedProducts = PRODUCT_REPO.search_product(productPattern)
        return render_template("product_choice.html", products=searchedProducts, user=current_user, productForm=productForm)
    # Else user did not search for product, just render the search bar and page
    products = PRODUCT_REPO.get_products()
    return render_template("product_choice.html", products=products, user=current_user, productForm=productForm)

@TICKET_API.route("/tickets", methods=["GET", "POST"])
@login_required
def show_ticket_products():
    productForm = SearchProductForm()
    # If user searched for product
    if productForm.validate_on_submit():
        productPattern = productForm.product.data
        searchedProducts = PRODUCT_REPO.search_product(productPattern)
        return render_template("product_choice2.html", products=searchedProducts, user=current_user, productForm=productForm)
    # Else user did not search for product, just render the search bar and page
    products = PRODUCT_REPO.get_products()
    return render_template("product_choice2.html", products=products, user=current_user, productForm=productForm)

@TICKET_API.route("/tickets/new/<int:productId>", methods=["GET", "POST"])
@login_required
def create_ticket(productId):
    # User selected the product to which the ticket will be created
    # here will be the ticket forms
    # Check if product exists
    if not PRODUCT_REPO.check_product(productId):
        abort(HTTP_NOT_FOUND)
    ticketForm = CreateTicketForm()
    # If user submitted new ticket
    if ticketForm.validate_on_submit():
        try:
            fileName = handle_image(ticketForm.image)
        except InvalidFile:
            return flash("Invalid file uploaded!")

        ticketTitle = ticketForm.title.data
        ticketDesc = ticketForm.description.data

        try:
            # Try to insert the new ticket but if something goes wrong, the image needs to be deleted
            # from filesystem
            TICKET_REPO.create_ticket(name=ticketTitle, description=ticketDesc, image=fileName, authorId=current_user.id, productId=productId)
        except Exception as e:
            remove_file(fileName)
        
        return redirect(url_for("dashboard.index"))

    return render_template("create_ticket.html", user=current_user, ticketForm=ticketForm, productId=productId)