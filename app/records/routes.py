from flask import render_template

from app.records import blueprint_records
from app.models.record import Record


@blueprint_records.route('/records')
def view_records():
    records = Record.query.all()
    return render_template('records.html', records=records)


@blueprint_records.route('/record-add')
def add_record():
    return render_template('record_add.html')


@blueprint_records.route('/record/<id>')
def edit_record(id):
    record = Record.query.filter_by(id=id).first()
    return render_template('record_edit.html', record=record)
