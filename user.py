from flask import Blueprint, request, jsonify, abort
from flask_login import login_required, current_user
from repositories.user_repository import UserRepository

USER_API = Blueprint("users", __name__)
USER_REPO = UserRepository()
HTTP_WRONG_INPUT = 400

ADMIN = 4
CUSTOMER = 0
COOKIE_POSITION = 99

@USER_API.route("/users", methods=["GET"])
@login_required
def users_json():
    try:
        userPattern = request.args.get("pattern")
        userPosition = int(request.args.get("position"))
    except TypeError:
        abort(HTTP_WRONG_INPUT)

    if userPosition == COOKIE_POSITION:
        # If there is special flag at position, the user search will be 
        # performed based on the position of user, who requested the search
        # and lower (So manager can search => managers, developers)
        # (Owner can search => owners, managers, developer)
        userPosition = current_user.position_id.id
        users = []
        for lowerPosition in range(0, (userPosition + 1)):
            positionUsers = USER_REPO.search_user(userPattern, lowerPosition)
            for positionUser in positionUsers:
                users.append({ positionUser.clientname: positionUser.id })

        result = {}
        result[COOKIE_POSITION] = users

        return jsonify(result)

    elif userPosition < CUSTOMER or userPosition > ADMIN:
        abort(HTTP_WRONG_INPUT)

    users = USER_REPO.search_user(userPattern, userPosition)
    result = {}
    result[userPosition] = []
    for user in users:
        result[userPosition].append(user.clientname)

    return jsonify(result)
