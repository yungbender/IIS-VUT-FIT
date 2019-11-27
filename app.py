from flask import Flask, render_template, request, make_response, render_template
from flask_login import current_user
import os
from datetime import timedelta
from login_manager import LOGIN_MANAGER
from mainpage import MAINPAGE_API
from login import LOGIN_API,SECRET_KEY
from register import REGISTER_API
from logout import LOGOUT_API
from ticket import TICKET_API
from dashboard import DASHBOARD_API
from profile import PROFILE_API
from product import PRODUCT_API
from user import USER_API
from task import TASK_API
from search import SEARCH_API
from upload_handler import MAX_UPLOAD_SIZE

from errors import error, not_permitted, page_not_found, wrong_request, internal_error


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder=os.path.join(os.getcwd(), "templates", "static"))

    app.register_blueprint(MAINPAGE_API)
    app.register_blueprint(LOGIN_API)
    app.register_blueprint(REGISTER_API)
    app.register_blueprint(LOGOUT_API)
    app.register_blueprint(DASHBOARD_API)
    app.register_blueprint(PROFILE_API)
    app.register_blueprint(PRODUCT_API)
    app.register_blueprint(TICKET_API)
    app.register_blueprint(USER_API)
    app.register_blueprint(TASK_API)
    app.register_blueprint(SEARCH_API)
    app.secret_key = SECRET_KEY
    app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_SIZE
    app.config["TRAP_HTTP_EXCEPTIONS"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
    LOGIN_MANAGER.init_app(app)
    
    return app
    
app = create_app()

@app.errorhandler(Exception)
def handle_error(e):
    if e.code == 400:
        return make_response(render_template("400.html", user=current_user), e.code)
    elif e.code == 401:
        return make_response(render_template("401.html", user=current_user), e.code)
    elif e.code == 403:
        return make_response(render_template("403.html", user=current_user), e.code)
    elif e.code == 404:
        return make_response(render_template("404.html", user=current_user), e.code)
    elif e.code == 500:
        return make_response(render_template("500.html", user=current_user), e.code)
    elif e.code > 400:
        return make_response(render_template("error.html", user=current_user), e.code)

def main():
    app.run(host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
