"""
Model for the records table
"""
from app.extensions import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.Date)
    date_finish = db.Column(db.Date)
    date_expire = db.Column(db.Date)
    record_valid = db.Column(db.Boolean)
    title = db.Column(db.String)
    description = db.Column(db.String)
    duration = db.Column(db.Time)
    duration_risk = db.Column(db.Time)
    duration_business = db.Column(db.Time)
    duration_practice = db.Column(db.Time)

    training_activity_id = db.Column(db.Integer, db.ForeignKey("training_activity.id"))
    training_type_id = db.Column(db.Integer, db.ForeignKey("training_type.id"))
    training_provider_id = db.Column(db.Integer, db.ForeignKey("training_provider.id"))
    training_location_id = db.Column(db.Integer, db.ForeignKey("training_location.id"))
