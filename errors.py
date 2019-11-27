from flask import render_template
from flask_login import current_user

def page_not_found(e):
    return render_template("404.html", user=current_user), 404

def not_permitted(e):
    return render_template("403.html", user=current_user), 403

def wrong_request(e):
    return render_template("400.html", user=current_user), 400

def internal_error(e):
    return render_template("500.html", user=current_user), 500

def error(e):
    return render_template("error.html", user=current_user)
