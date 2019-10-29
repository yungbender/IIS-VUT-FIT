from flask import Blueprint, request, jsonify
from flask_login import login_required
from repositories.user_repository import UserRepository

MANAGERS_API = Blueprint("manager", __name__)
USER_REPO = UserRepository()

@MANAGERS_API.route("/managers", methods=["GET"])
@login_required
def managers_json():
    managerPattern = request["pattern"]
    managers = USER_REPO.get_managers(managerPattern)
    result = {}
    result["managers"] = []
    for manager in managers:
        result["managers"].append(manager)
    
    return jsonify(json)
