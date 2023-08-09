"""
Model for the Training EA Division table
- EAust Training division
"""
from app.extensions import db


class TrainingDivision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String)
