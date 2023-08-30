"""
Model for the Training Activity table
- the type of training i.e. Presentation, workshop
"""
from app.extensions import db


class TrainingActivity(db.Model):
    __tablename__ = "training_activity"

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String)
    description = db.Column(db.String)
