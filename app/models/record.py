"""
Model for the records table
"""
from app.extensions import db


class Record(db.Model):
    __tablename__ = "record"

    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.Date)
    date_finish = db.Column(db.Date)
    date_expire = db.Column(db.Date)
    record_valid = db.Column(db.Boolean)
    title = db.Column(db.String)
    description = db.Column(db.String)
    notes = db.Column(db.String)
    duration = db.Column(db.Time)
    duration_risk = db.Column(db.Time)
    duration_business = db.Column(db.Time)
    duration_practice = db.Column(db.Time)
    training_provider = db.Column(db.String)
    training_location = db.Column(db.String)
    training_activity_id = db.Column(db.Integer, db.ForeignKey("training_activity.id"))
    training_type_id = db.Column(db.Integer, db.ForeignKey("training_type.id"))
    training_division_id = db.Column(db.Integer, db.ForeignKey("training_division.id"))

    # Foreign key relationship
    training_activity = db.relationship("TrainingActivity", backref="Record",
                                        foreign_keys=[training_activity_id])
    training_type = db.relationship("TrainingType", backref="Record",
                                    foreign_keys=[training_type_id])
    training_division = db.relationship("TrainingDivision", backref="Record",
                                        foreign_keys=[training_division_id])

    def __init__(self):
        # set to true for new records, assumes they are still valid
        self.record_valid = True
