from flask import Blueprint, render_template, abort, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from repositories.ticket_repository import TicketRepository
from repositories.product_repository import ProductRepository
from repositories.comment_repository import CommentRepository
from templates.create_ticket import CreateTicketForm
from templates.search_product import SearchProductForm
from templates.create_comment_ticket import CreateCommentForm
from upload_handler import handle_image, InvalidFile, remove_file
from utilities import format_date, make_thumbnail
from peewee import PeeweeException

TICKET_API = Blueprint("ticket", __name__)
TICKET_REPO = TicketRepository()
PRODUCT_REPO = ProductRepository()
COMMENT_REPO = CommentRepository()
HTTP_NOT_FOUND = 404
HTTP_FORBIDDEN = 403
HTTP_BAD_REQUEST = 400
ADMIN = 4
OWNER = 3
MANAGER = 2
DEVELOPER = 1
TICKET_THUMBNAIL_MAX_LENGTH = 64
AUTHOR_THUMBNAIL_MAX_LENGTH = 15

@TICKET_API.route("/tickets/<int:productId>/<int:ticketId>", methods=["GET", "POST"])
def product_ticket(productId, ticketId):
    ticketForm = CreateTicketForm()
    commentForm = CreateCommentForm()

    # Product exists
    if PRODUCT_REPO.check_product(productId):
        # Get the ticket
        ticket = TICKET_REPO.get_ticket(ticketId)
        # Ticket exists
        if ticket:
            # Get ticket comments
            # If ticket form was sent, update the ticket
            if ticketForm.validate_on_submit():
                ticket.name = ticketForm.title.data
                ticket.description = ticketForm.description.data
                try:
                    ticket.save()
                except PeeweeException:
                    flash("Cannot save! Check length of elements!", "ticket")

            # If comment form was sent, create new comment
            elif commentForm.validate_on_submit():
                if ticket.closed == True:
                    return abort(HTTP_BAD_REQUEST)
                try:
                    imageName = handle_image(commentForm.image)
                except Exception as e:
                    remove_file(imageName)
                    return flash("Invalid image uploaded!", "ticket")

                comment = commentForm.content.data
                try:
                    COMMENT_REPO.create_ticket_comment(comment, imageName, ticketId, current_user.id)
                except PeeweeException:
                    flash("Cannot save! Check length of elements!", "ticket")
            # Else just return prefilled forms to enable editing

            comments = COMMENT_REPO.get_ticket_comments(ticketId)
            format_date(ticket)
            for comment in comments:
                format_date(comment)
            ticketForm.description.data = ticket.description
            ticketForm.title.data = ticket.name

            return render_template("ticket.html", ticketForm=ticketForm, user=current_user, ticket=ticket, comments=comments, commentForm=commentForm)
    return abort(HTTP_NOT_FOUND)

@TICKET_API.route("/tickets/<int:productId>", methods=["GET"])
def product_tickets(productId):
    if PRODUCT_REPO.check_product(productId):
        tickets = TICKET_REPO.get_product_tickets(productId)
        for ticket in tickets:
            ticket.name = make_thumbnail(ticket.name, TICKET_THUMBNAIL_MAX_LENGTH)
            ticket.author_id.username = make_thumbnail(ticket.author_id.clientname, AUTHOR_THUMBNAIL_MAX_LENGTH)
            format_date(ticket)
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
            return flash("Invalid file uploaded!", "ticket")

        ticketTitle = ticketForm.title.data
        ticketDesc = ticketForm.description.data

        try:
            # Try to insert the new ticket but if something goes wrong, the image needs to be deleted
            # from filesystem
            TICKET_REPO.create_ticket(name=ticketTitle, description=ticketDesc, image=fileName, authorId=current_user.id, productId=productId)
        except PeeweeException:
            flash("Cannot save! Check length of elements!", "ticket")
            return render_template("create_ticket.html", user=current_user, ticketForm=ticketForm, productId=productId)
        except Exception as e:
            remove_file(fileName)
        
        return redirect(url_for("dashboard.index"))

    return render_template("create_ticket.html", user=current_user, ticketForm=ticketForm, productId=productId)

@TICKET_API.route("/tickets/<int:productId>/<int:ticketId>/<int:commentId>")
@login_required
def ticket_answer(productId, ticketId, commentId):
    if PRODUCT_REPO.check_product(productId):
        ticket = TICKET_REPO.get_ticket(ticketId)
        if ticket:
            if ticket.closed == True:
                return abort(HTTP_BAD_REQUEST)
            elif ticket.author_id.id != current_user.id and current_user.position_id.id < 2:
                abort(HTTP_FORBIDDEN)
            comment = COMMENT_REPO.get_comment(commentId)
            if comment:
                comment.answer = True
                comment.save()

                return redirect("/tickets/" + str(productId) + "/" + str(ticketId))

    return abort(HTTP_NOT_FOUND)

@TICKET_API.route("/tickets/<int:productId>/<int:ticketId>/close")
@login_required
def ticket_close(productId, ticketId):
    if PRODUCT_REPO.check_product(productId):
        ticket = TICKET_REPO.get_ticket(ticketId)
        if ticket:
            if ticket.closed == True:
                return abort(HTTP_BAD_REQUEST)
            elif ticket.author_id.id != current_user.id and current_user.position_id.id < 2:
                return abort(HTTP_FORBIDDEN)
            ticket.closed = True
            ticket.save()

            flash("Ticket closed!")

            return redirect("/tickets/" + str(productId) + "/" + str(ticketId))

    return abort(HTTP_NOT_FOUND)

@TICKET_API.route("/tickets/json")
@login_required
def ticket_json():
    result = {}
    if current_user.position_id.id < MANAGER:
        return abort(HTTP_FORBIDDEN)
    elif current_user.position_id.id == MANAGER:
        products = PRODUCT_REPO.get_product_manager(current_user.id)
    elif current_user.position_id.id == OWNER:
        products = PRODUCT_REPO.get_product_owner(current_user.id)
    elif current_user.position_id.id == ADMIN:
        products = PRODUCT_REPO.get_products()

    for product in products:
        productTickets = TICKET_REPO.get_product_tickets(product.id)
        if product_tickets:
            result[product.name] = []
            for ticket in productTickets:
                result[product.name].append({ticket.name:ticket.id}) 
    
    return jsonify(result)

