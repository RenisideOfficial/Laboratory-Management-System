from flask import Blueprint
from app.services import result_services
from app.middlewares.middleware import token_required

bp = Blueprint("result_routes", __name__)

bp.get("/patient/<int:patient_id>")(token_required(result_services.get_results_by_patient))
