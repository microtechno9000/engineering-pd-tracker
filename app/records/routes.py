from flask import render_template

from app.records import blueprint_records
from app.models.record import Record


@blueprint_records.route('/records')
def media():
    records = Record.query.all()
    return render_template('records.html', records=records)
