"""
Model for the Training Type table
- The EA Training Type (1 through 6)
"""
from app.extensions import db


class TrainingType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    description = db.Column(db.String)
    conditions = db.Column(db.String)
