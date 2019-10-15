from flask import Flask, render_template, request
from login_manager import LOGIN_MANAGER
from mainpage import MAINPAGE_API
from login import LOGIN_API,SECRET_KEY
from register import REGISTER_API
from logout import LOGOUT_API
from ticket import TICKET_API
from dashboard import DASHBOARD_API
import os


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder=os.path.join(os.getcwd(), "templates", "static"))

    app.register_blueprint(MAINPAGE_API)
    app.register_blueprint(LOGIN_API)
    app.register_blueprint(REGISTER_API)
    app.register_blueprint(LOGOUT_API)
    app.register_blueprint(TICKET_API)
    app.register_blueprint(DASHBOARD_API)
    app.secret_key = SECRET_KEY
    app.config["REMEMBER_COOKIE_DURATION"] = 10
    LOGIN_MANAGER.init_app(app)
    
    return app
    
app = create_app()

def main():
    app.run(host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
