from flask import Blueprint
from internal.services import user_services

bp = Blueprint("auth_routes", __name__)

bp.post("/register")(user_services.register_user)
bp.post("/login")(user_services.login_user)
