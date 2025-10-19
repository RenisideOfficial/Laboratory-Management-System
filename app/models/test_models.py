from datetime import datetime
from app.models.test_models import db
from pydantic import BaseModel

# Models section
class Test(db.Model):
    __tablename__ = "tests"

    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(100), nullable=False)
    result = db.Column(db.Text)
    status = db.Column(db.String(50), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))
    performed_by = db.Column(db.Integer, db.ForeignKey("users.id"))

    patient = db.relationship("Patient", backref="tests")
    performer = db.relationship("User", backref="tests_performed")

    def __repr__(self):
        return f"<Test {self.test_name} for Patient {self.patient_id}>"

# Schemas section
class TestCreate(BaseModel):
    test_name: str
    patient_id: int
    performed_by: int

class TestResponse(BaseModel):
    id: int
    test_name: str
    result: str | None
    status: str
    patient_id: int
    performed_by: int
    created_at: datetime

    class Config:
        orm_mode = True
