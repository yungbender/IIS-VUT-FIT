from flask import Flask, render_template, request
from mainpage import MAINPAGE_API

def create_app():
    app = Flask(__name__, template_folder="templates")
    
    app.register_blueprint(MAINPAGE_API)
    
    return app

    
app = create_app()

def main():
    app.run(host="0.0.0.0", port=6969)

if __name__ == "__main__":
    main()
