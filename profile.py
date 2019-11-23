from flask import Blueprint, render_template, abort, flash, redirect
from flask_login import login_required, current_user
from models.user import User
from repositories.user_repository import UserRepository
from templates.profile import EditProfileForm
from upload_handler import handle_image, remove_file

PROFILE_API = Blueprint("profile", __name__)
USER_REPO = UserRepository()
HTTP_NOT_FOUND = 404
HTTP_FORBIDDEN = 403

@PROFILE_API.route("/profile/<int:userId>", methods=["GET"])
def profile(userId):
    user = USER_REPO.get_user(userId)
    userForm = EditProfileForm()
    if user:
        userForm.mail.data = user.mail
        userForm.name.data = user.name
        userForm.surname.data = user.surname
        userForm.birth.data = user.birth
        userForm.position.data = user.position_id

        return render_template("profile.html", user=current_user, userForm=userForm, shownUser=user)

    return abort(HTTP_NOT_FOUND)

@PROFILE_API.route("/profile/<int:userId>", methods=["POST"])
@login_required
def profile_edit(userId):
    user = USER_REPO.get_user(userId)
    if current_user.id != user.id:
        return abort(HTTP_FORBIDDEN)

    userForm = EditProfileForm() 

    if user:
        if userForm.validate_on_submit():
            uploadOK = False
            user.mail = userForm.mail.data
            user.name = userForm.name.data
            user.surname = userForm.surname.data
            user.birth = userForm.birth.data
            user.position_id = userForm.position.data
            try:
                imageName = handle_image(userForm.image)
                uploadOK = True
            except Exception as e:
                flash("Wrong image uploaded!")
                remove_file(imageName)
            
            if uploadOK:
                user.image = imageName
            
            user.save()

            return redirect("/profile/" + str(userId))
