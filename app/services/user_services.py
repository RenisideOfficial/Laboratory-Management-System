from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from db.db import db
from app.models.user_models import User
import jwt
import datetime
from config.config import Config

def register_user():
    """Register a new user (doctor/staff/admin)"""
    data = request.get_json()

    if not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password are required"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400

    hashed_pw = generate_password_hash(data["password"])
    user = User(
        full_name=data["full_name"],
        email=data["email"],
        password_hash=hashed_pw,
        role=data.get("role", "staff"),
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


def login_user():
    """Authenticate and return JWT token"""
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()

    if not user or not check_password_hash(user.password_hash, data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6)
        },
        Config.SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({"token": token, "user": {"id": user.id, "name": user.full_name, "role": user.role}})
