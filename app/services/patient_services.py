from flask import jsonify, request
from db.db import db
from app.models.patient_models import Patient

def create_patient(user_id):
    """Add a new patient"""
    data = request.get_json()
    patient = Patient(
        name=data["name"],
        date_of_birth=data["date_of_birth"],
        gender=data["gender"],
        contact_info=data.get("contact_info"),
        created_by=user_id
    )
    db.session.add(patient)
    db.session.commit()

    return jsonify({"message": "Patient added successfully", "patient_id": patient.id}), 201


def get_patients(user_id):
    """Fetch all patients"""
    patients = Patient.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "gender": p.gender,
            "date_of_birth": p.date_of_birth.isoformat(),
            "contact_info": p.contact_info,
            "created_at": p.created_at.isoformat()
        } for p in patients
    ])


def get_patient(user_id, patient_id):
    """Fetch single patient"""
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "gender": patient.gender,
        "date_of_birth": patient.date_of_birth.isoformat(),
        "contact_info": patient.contact_info
    })


def update_patient(user_id, patient_id):
    """Update patient details"""
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        if hasattr(patient, key):
            setattr(patient, key, value)
    db.session.commit()

    return jsonify({"message": "Patient updated successfully"})


def delete_patient(user_id, patient_id):
    """Delete a patient"""
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted"})
