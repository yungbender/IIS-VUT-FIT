from flask import Blueprint, render_template, abort, flash, redirect
from flask_login import login_required, current_user
from models.user import User
from repositories.user_repository import UserRepository
from templates.profile import EditProfileForm
from templates.profile_admin import EditProfileFormAdmin
from upload_handler import handle_image, remove_file
from utilities import format_date

PROFILE_API = Blueprint("profile", __name__)
USER_REPO = UserRepository()
HTTP_NOT_FOUND = 404
HTTP_FORBIDDEN = 403
ADMIN = 4

@PROFILE_API.route("/profile/<int:userId>", methods=["GET"])
def profile(userId):
    user = USER_REPO.get_user(userId)
    if user and current_user.position_id.id < ADMIN:
        userForm = EditProfileForm()
        userForm.mail.data = user.mail
        userForm.name.data = user.name
        userForm.surname.data = user.surname

        return render_template("profile.html", user=current_user, userForm=userForm, shownUser=user)

    elif user:
        print("generujem adminovsku")
        userForm = EditProfileFormAdmin()
        userForm.mail.data = user.mail
        userForm.name.data = user.name
        userForm.surname.data = user.surname
        userForm.position.data = user.position_id.id

        return render_template("profile.html", user=current_user, userForm=userForm, shownUser=user)

    return abort(HTTP_NOT_FOUND)

@PROFILE_API.route("/profile/<int:userId>", methods=["POST"])
@login_required
def profile_edit(userId):
    user = USER_REPO.get_user(userId)
    if current_user.id != user.id and current_user.position_id.id < ADMIN:
        return abort(HTTP_FORBIDDEN)

    userForm = EditProfileForm()
    userFormAdmin = EditProfileFormAdmin()

    if user:
        if userFormAdmin.validate_on_submit():
            uploadOK = False
            mail = userFormAdmin.mail.data
            name = userFormAdmin.name.data
            surname = userFormAdmin.surname.data
            position = userFormAdmin.position.data
            try:
                imageName = handle_image(userFormAdmin.image)
                uploadOK = True
            except Exception as e:
                flash("Wrong image uploaded!", "profile")
                remove_file(imageName)
            
            if uploadOK and imageName:
                user.image = imageName
            
            USER_REPO.update_user(user.id, mail, name, surname, position)
        elif userForm.validate_on_submit():
            uploadOK = False
            mail = userForm.mail.data
            name = userForm.name.data
            surname = userForm.surname.data
            try:
                imageName = handle_image(userForm.image)
                uploadOK = True
            except Exception as e:
                flash("Wrong image uploaded!", "profile")
                remove_file(imageName)
            
            if uploadOK:
                USER_REPO.update_user(user.id, mail, name, surname, user.position_id.id, image=imageName)
            else:
                USER_REPO.update_user(user.id, mail, name, surname, user.position_id.id)
                

        return redirect("/profile/" + str(userId))

    return abort(HTTP_NOT_FOUND)