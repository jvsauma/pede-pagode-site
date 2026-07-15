from flask import Blueprint

from backend.controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

controller = AuthController()


@auth_bp.get("/login")
def exibir_login():

    return controller.exibir_login()


@auth_bp.post("/login")
def login():

    return controller.login()
