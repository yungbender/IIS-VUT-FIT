from flask import Blueprint, request, jsonify, abort
from flask_login import login_required
from repositories.user_repository import UserRepository

MANAGER_API = Blueprint("managers", __name__)
USER_REPO = UserRepository()
HTTP_WRONG_INPUT = 400

@MANAGER_API.route("/managers", methods=["GET"])
@login_required
def managers_json():
    managerPattern = request.args.get("pattern")
    if managerPattern is None:
        return abort(HTTP_WRONG_INPUT)

    managers = USER_REPO.search_managers(managerPattern)
    result = {}
    result["managers"] = []
    for manager in managers:
        result["managers"].append(manager.clientname)
    
    return jsonify(result)
