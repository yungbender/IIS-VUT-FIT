from flask import request
from werkzeug import secure_filename
from os.path import join
from os import remove, listdir, getcwd

ALLOWED_UPLOAD_EXTENSIONS = ["png", "jpg", "gif"]
MAX_UPLOAD_SIZE = 5 * 1024 * 1024 # 5 MB
UPLOAD_FOLDER = "/templates/static/uploads/"

# The upload folder is for user uploads, every upload is named by name
# <number>.<extension> starting from 3
# 1 is reserved for default profile picture
# 2 is reserved for default product picture

class InvalidFile(BaseException):
    pass

def generate_image_name():
    # Sort the list of files in uploads folder desceding
    cwd = getcwd()
    images = listdir(cwd + UPLOAD_FOLDER)
    imageNumbers = []
    for image in images:
        imageNumbers.append(int(image.split(".")[0]))

    lastImage = sorted(imageNumbers, reverse=True)[0]
    # Split the image name and increment its number name
    # for ex. 10.jpg
    # ["10", "jpg"]
    # increment the number and return it
    return lastImage + 1

def handle_image(file):
    # Get filename
    if file.data == None:
        return None
        
    fileName = secure_filename(file.data.filename)
    if fileName == "":
        return None
    # Check if it is seriously image
    fileExtension = (fileName.split(".")[-1]).lower()
    if fileExtension not in ALLOWED_UPLOAD_EXTENSIONS:
        raise InvalidFile
    newName = generate_image_name()
    newName = str(newName) + "." + fileExtension
    cwd = getcwd()
    savePath = cwd + UPLOAD_FOLDER + newName
    # Save image
    file.data.save(savePath)
    return newName

def remove_file(fileName):
    # Method removes file from upload folder
    cwd = getcwd()
    remove(cwd + UPLOAD_FOLDER + fileName)