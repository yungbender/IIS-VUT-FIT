from flask import Blueprint, render_template, abort, flash, redirect
from flask_login import login_required, current_user
from models.user import User
from repositories.user_repository import UserRepository
from templates.profile import EditProfileForm
from templates.profile_admin import EditProfileFormAdmin
from upload_handler import handle_image, remove_file, InvalidFile
from utilities import format_date
from peewee import PeeweeException

PROFILE_API = Blueprint("profile", __name__)
USER_REPO = UserRepository()
HTTP_NOT_FOUND = 400
HTTP_FORBIDDEN = 403
ADMIN = 4

@PROFILE_API.route("/profile/<int:userId>", methods=["GET"])
def profile(userId):
    user = USER_REPO.get_user(userId)
    if current_user.is_authenticated:
        if user and current_user.position_id.id < ADMIN:
            userForm = EditProfileForm()
            userForm.mail.data = user.mail
            userForm.name.data = user.name
            userForm.surname.data = user.surname

            return render_template("profile.html", user=current_user, userForm=userForm, shownUser=user)

    if user:
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
            except InvalidFile:
                flash("Wrong image uploaded!", "profile")
                return render_template("profile.html", user=current_user, userForm=userFormAdmin, shownUser=user)

            try:
                if uploadOK and imageName:
                    USER_REPO.update_user(user.id, mail, name, surname, position, image=imageName)
                else:
                    USER_REPO.update_user(user.id, mail, name, surname, position)
            except PeeweeException:
                flash("Cannot save! Check length of elements!", "profile")
                return render_template("profile.html", user=current_user, userForm=userFormAdmin, shownUser=user)

        elif userForm.validate_on_submit():
            uploadOK = False
            mail = userForm.mail.data
            name = userForm.name.data
            surname = userForm.surname.data
            try:
                imageName = handle_image(userForm.image)
                uploadOK = True
            except InvalidFile:
                flash("Wrong image uploaded!", "profile")
                return render_template("profile.html", user=current_user, userForm=userForm, shownUser=user)
            
            try:
                if uploadOK and imageName:
                    USER_REPO.update_user(user.id, mail, name, surname, user.position_id.id, image=imageName)
                else:
                    USER_REPO.update_user(user.id, mail, name, surname, user.position_id.id)
            except PeeweeException:
                flash("Cannot save! Check length of elements!", "profile")
                return render_template("profile.html", user=current_user, userForm=userForm, shownUser=user)
                

        return redirect("/profile/" + str(userId))

    return abort(HTTP_NOT_FOUND)