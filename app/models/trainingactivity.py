"""
Model for the Training Activity table
"""
from app.extensions import db


class TrainingActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.string)
    description = db.Column(db.string)
