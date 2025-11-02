import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Global configuration for LabMS"""

    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    # MySQL connection
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
