from flask import jsonify, request
from db.db import db
from app.models.test_models import Test

def create_test():
    """Assign a test to a patient"""
    data = request.get_json()

    test = Test(
        test_name=data["test_name"],
        patient_id=data["patient_id"],
        performed_by=data["performed_by"],
        status=data.get("status", "pending")
    )

    db.session.add(test)
    db.session.commit()

    return jsonify({"message": "Test created successfully", "test_id": test.id}), 201


def get_tests():
    """Fetch all tests"""
    tests = Test.query.all()
    return jsonify([
        {
            "id": t.id,
            "test_name": t.test_name,
            "patient_id": t.patient_id,
            "status": t.status,
            "created_at": t.created_at.isoformat(),
        } for t in tests
    ])


def get_test(test_id):
    """Fetch a single test"""
    test = Test.query.get(test_id)
    if not test:
        return jsonify({"error": "Test not found"}), 404

    return jsonify({
        "id": test.id,
        "test_name": test.test_name,
        "status": test.status,
        "result": test.result,
        "patient_id": test.patient_id,
        "performed_by": test.performed_by,
        "created_at": test.created_at.isoformat(),
    })


def update_test(test_id):
    """Update a test result or status"""
    test = Test.query.get(test_id)
    if not test:
        return jsonify({"error": "Test not found"}), 404

    data = request.get_json()
    if "result" in data:
        test.result = data["result"]
    if "status" in data:
        test.status = data["status"]

    db.session.commit()
    return jsonify({"message": "Test updated successfully"})
