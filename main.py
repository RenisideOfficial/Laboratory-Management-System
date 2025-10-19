from flask import Flask
from db.db import init_db
# from app.routes.user_route import user_bp
# from app.routes.patient_route import patient_bp
# from app.routes.test_route import test_bp

def create_app():
    app = Flask(__name__)

    # Initialize database
    init_db(app)

    # Register blueprints
    # app.register_blueprint(user_bp)
    # app.register_blueprint(patient_bp)
    # app.register_blueprint(test_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
