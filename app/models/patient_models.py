from pydantic import BaseModel, EmailStr
from app.models.patient_models import db
from datetime import datetime, date

# Models section
class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    contact_info = db.Column(db.String(255))
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))  # registered doctors or staff
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    creator = db.relationship("User", backref="patients")

    def __repr__(self):
        return f"<Patient {self.name}>"

# Schemas section
class PatientCreate(BaseModel):
    name: str
    date_of_birth: date
    gender: str
    contact_info: str | None = None
    created_by: int

class PatientResponse(BaseModel):
    id: int
    name: str
    date_of_birth: date
    gender: str
    contact_info: str | None
    created_at: datetime

    class Config:
        orm_mode = True