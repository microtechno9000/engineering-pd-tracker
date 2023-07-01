from app.extensions import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.Date)
    date_finish = db.Column(db.Date)
    duration = db.Column(db.Time)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f"{self.title}"
