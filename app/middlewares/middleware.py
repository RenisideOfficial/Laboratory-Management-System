from flask_cors import CORS
from flask import request, jsonify
from functools import wraps
import jwt
from config.config import Config

def register_middlewares(app):
    """Register global middlewares"""
    CORS(app)

    @app.before_request
    def log_request():
        app.logger.info(f"{request.method} {request.path}")

    return app


def token_required(f):
    """JWT authentication middleware"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"error": "Token missing"}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            user_id = data["user_id"]
        except Exception as e:
            return jsonify({"error": f"Invalid token: {str(e)}"}), 401

        return f(user_id, *args, **kwargs)
    return decorated
