"""
Routes for records pages
"""
from datetime import datetime, date

from flask import render_template, request, redirect, current_app
from flask_sqlalchemy import get_debug_queries

from app.extensions import db
from app.models.record import Record
from app.models.trainingactivity import TrainingActivity
from app.models.trainingdivision import TrainingDivision
from app.models.trainingtype import TrainingType
from app.records import blueprint_records
from app.records.forms import FormRecord


@blueprint_records.route('/records')
def view_records():
    records = Record.query.all()

    info = get_debug_queries()[0]
    print(info.statement, info.parameters)

    return render_template('records.html', records=records)


@blueprint_records.route('/record-add', methods=('GET', 'POST'))
def add_record():
    # new record WTForm validation
    recordform = FormRecord()
    recordform = form_select_data(recordform)
    # get today's date
    date_today = date.today()

    current_app.logger.debug(request.form)

    if recordform.validate_on_submit():
        record = Record()
        save_record(record, recordform)
        # return to record page
        return redirect('/records')
    else:
        current_app.logger.debug("GET - no valid POST data")

        return render_template('record_add.html',
                               form=recordform, date_today=date_today)


@blueprint_records.route('/record/<record_id>', methods=('GET', 'POST'))
def edit_record(record_id):
    record = Record.query.filter_by(id=record_id).first()

    # new record WTForm validation
    recordform = FormRecord(request.values, obj=record)
    recordform = form_select_data(recordform)

    # get today's date
    date_today = date.today()

    if recordform.validate_on_submit():
        current_app.logger.debug('Saving edit')
        save_record(record, recordform)
        # return to record page
        return redirect('/records')
    else:
        recordform.training_activity_id.default = record.training_activity_id
        recordform.training_type_id.default = record.training_type_id
        recordform.training_division_id.default = record.training_division_id

    current_app.logger.debug(recordform.training_activity_id.default)

    return render_template('record_add.html',
                           form=recordform, date_today=date_today)


def save_record(record, form):
    # save
    current_app.logger.debug("Saving record")

    # total duration, sum of each area
    duration_risk = datetime.strptime(form.duration_risk.data, "%H:%M:%S")
    duration_business = datetime.strptime(form.duration_business.data, "%H:%M:%S")
    duration_practice = datetime.strptime(form.duration_practice.data, "%H:%M:%S")
    duration = duration_risk

    # set the new record datatype
    record.date_start = form.date_start.data
    record.date_finish = form.date_finish.data
    record.date_expire = form.date_finish.data
    record.title = form.title.data
    record.description = form.description.data
    record.notes = form.notes.data
    record.training_provider = form.training_provider.data
    record.training_location = form.training_location.data
    record.duration = duration.time()
    record.duration_risk = duration_risk.time()
    record.duration_business = duration_business.time()
    record.duration_practice = duration_practice.time()
    record.training_type_id = form.training_type_id.data
    record.training_activity_id = form.training_activity_id.data
    record.training_division_id = form.training_division_id.data

    # save data to DB
    db.session.add(record)
    db.session.commit()


def form_select_data(form):
    # get form values
    trg_activity = TrainingActivity.query.all()
    trg_type = TrainingType.query.all()
    trg_division = TrainingDivision.query.all()

    form.training_activity_id.choices = [(act.id, act.activity) for act in trg_activity]
    form.training_type_id.choices = [(act.id, act.type) for act in trg_type]
    form.training_division_id.choices = [(act.id, act.division) for act in trg_division]

    return form
