from flask import Flask
from config.config import Config
from db.db import init_db
from internal.middlewares.middleware import register_middlewares
from internal.routes import user_routes, patient_routes, test_routes, result_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB
    init_db(app)

    # Create all tables
    from db.db import db
    with app.app_context():
        db.create_all()

    # Register middlewares
    register_middlewares(app)

    # Register all routes
    app.register_blueprint(user_routes.bp, url_prefix="/api/auth")
    app.register_blueprint(patient_routes.bp, url_prefix="/api/patients")
    app.register_blueprint(test_routes.bp, url_prefix="/api/tests")
    app.register_blueprint(result_routes.bp, url_prefix="/api/results")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)
