"""
Model for the Training Location table
"""
from app.extensions import db


class TrainingLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    notes = db.Column(db.String)
