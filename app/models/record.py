"""
Model for the records table
"""
from app.extensions import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.Date)
    date_finish = db.Column(db.Date)
    date_expire = db.Column(db.Date)
    title = db.Column(db.String)
    description = db.Column(db.String)
    duration = db.Column(db.Time)
    duration_risk = db.Column(db.Time)
    duration_business = db.Column(db.Time)
    duration_practice = db.Column(db.Time)
