from flask import Flask, render_template, request
from mainpage import MAINPAGE_API
from login import LOGIN_API,SECRET_KEY
from login_manager import LOGIN_MANAGER


def create_app():
    app = Flask(__name__, template_folder="templates")
    
    app.register_blueprint(MAINPAGE_API)
    app.register_blueprint(LOGIN_API)
    app.secret_key = SECRET_KEY

    LOGIN_MANAGER.init_app(app)
    
    return app

    
app = create_app()

def main():
    app.run(host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
