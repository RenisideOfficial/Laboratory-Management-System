from flask import Blueprint
from app.services import test_services
from app.middlewares.middleware import token_required

bp = Blueprint("test_routes", __name__)

bp.post("/")(token_required(test_services.create_test))
bp.get("/")(token_required(test_services.get_tests))
bp.get("/<int:test_id>")(token_required(test_services.get_test))
bp.put("/<int:test_id>")(token_required(test_services.update_test))
