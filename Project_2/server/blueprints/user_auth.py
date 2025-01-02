from flask import Blueprint


user_auth_bp = Blueprint("user_auth", __name__, template_folder = "../client/src/templates/user_auth")

@user_auth_bp.route("/")
def index():
    return "This will be the default page"