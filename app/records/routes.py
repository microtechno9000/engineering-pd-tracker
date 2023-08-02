from flask import render_template

from app.records import blueprint_records
from app.models.record import Record
from app.models.trainingtype import TrainingType
from app.models.trainingactivity import TrainingActivity


@blueprint_records.route('/records')
def view_records():
    records = Record.query.all()
    return render_template('records.html', records=records)


@blueprint_records.route('/record-add')
def add_record():
    trg_activity = TrainingActivity.query.all()
    trg_type = TrainingType.query.all()
    return render_template('record_add.html',
                           trg_type=trg_type, trg_activity=trg_activity)


@blueprint_records.route('/record/<id>')
def edit_record(id):
    record = Record.query.filter_by(id=id).first()
    return render_template('record_edit.html', record=record)
