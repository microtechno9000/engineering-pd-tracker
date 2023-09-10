"""
Model for the Training Provider table
"""
from app.extensions import db


class TrainingProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    notes = db.Column(db.String)
