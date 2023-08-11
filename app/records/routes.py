"""
Routes for records pages
"""
from flask import render_template, request, redirect
from datetime import date

from app.records import blueprint_records
from app.models.record import Record
from app.models.trainingtype import TrainingType
from app.models.trainingactivity import TrainingActivity
from app.models.trainingeadivision import TrainingDivision
from app.records.forms import NewRecord


@blueprint_records.route('/records')
def view_records():
    records = Record.query.all()
    return render_template('records.html', records=records)


@blueprint_records.route('/record-add', methods=('GET', 'POST'))
def add_record():
    record_form = NewRecord()

    if request.method == 'POST':
        record_form.validate_on_submit()
        # save data to DB
        return redirect('/records')
    else:
        # get form values
        trg_activity = TrainingActivity.query.all()
        trg_type = TrainingType.query.all()
        trg_division = TrainingDivision.query.all()

        # get today's date
        date_today = date.today()

        return render_template('record_add.html',
                               form=record_form,
                               trg_type=trg_type, trg_activity=trg_activity, trg_division=trg_division,
                               date_today=date_today)


@blueprint_records.route('/record/<record_id>')
def edit_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    return render_template('record_edit.html', record=record)
