from flask import Blueprint
from app.services import patient_services
from app.middlewares.middleware import token_required

bp = Blueprint("patient_routes", __name__)

bp.post("/")(token_required(patient_services.create_patient))
bp.get("/")(token_required(patient_services.get_patients))
bp.get("/<int:patient_id>")(token_required(patient_services.get_patient))
bp.put("/<int:patient_id>")(token_required(patient_services.update_patient))
bp.delete("/<int:patient_id>")(token_required(patient_services.delete_patient))
