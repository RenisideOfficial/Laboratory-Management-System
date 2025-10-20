from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, EmailStr
from datetime import datetime
from db.db import db

# Models section
class User(db.Model):
    __tablename__ = "users"

    # Data representation and transfer (DTO)
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="staff")  # any personel
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # for debugging/logging purposes
    def __repr__(self):
        return f"<User {self.full_name}>"

# Schemas section
class UserCreate(BaseModel):
    """Data handling and validation"""
    full_name: str
    email: EmailStr
    password: str
    role: str = "staff"

class UserResponse(BaseModel):
    """User response model"""
    id: int
    full_name: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        # allow reading SQLAlchemy objects directly
        orm_mode = True

