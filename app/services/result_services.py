from flask import jsonify
from app.models.test_models import Test

def get_results_by_patient(patient_id):
    """Fetch all results for a specific patient"""
    tests = Test.query.filter_by(patient_id=patient_id).all()
    if not tests:
        return jsonify({"error": "No tests found for this patient"}), 404

    results = []
    for t in tests:
        results.append({
            "test_name": t.test_name,
            "status": t.status,
            "result": t.result,
            "created_at": t.created_at.isoformat()
        })

    return jsonify({"patient_id": patient_id, "results": results})
