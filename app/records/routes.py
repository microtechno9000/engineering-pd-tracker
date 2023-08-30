"""
Routes for records pages
"""
from flask import render_template, request, redirect, current_app
from datetime import date, datetime, timedelta
from flask_sqlalchemy import get_debug_queries

from app.records import blueprint_records
from app.models.record import Record
from app.models.trainingtype import TrainingType
from app.models.trainingactivity import TrainingActivity
from app.models.trainingdivision import TrainingDivision
from app.records.forms import FormRecord
from app.extensions import db


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
    # get today's date
    date_today = date.today()

    current_app.logger.debug(request.form)

    if recordform.validate_on_submit():
        current_app.logger.debug(request.form)
        current_app.logger.debug("POST - proces data")

        # set the dates in datetime format
        date_start = datetime.strptime(request.form['recordStartDate'], "%Y-%m-%d")
        date_finish = datetime.strptime(request.form['recordFinishDate'], "%Y-%m-%d")
        date_expire = date_finish + timedelta(days=(365 * 3))
        # total duration, sum of each area
        time_risk = datetime.strptime(request.form['recordTimeRisk'], "%H:%M:%S")
        time_business = datetime.strptime(request.form['recordTimeBusiness'], "%H:%M:%S")
        time_aop = datetime.strptime(request.form['recordTimeAop'], "%H:%M:%S")
        duration = time_risk
        # link to foreign tables
        training_type = TrainingType().query.filter_by(type=request.form['recordType']).first()
        training_activity = TrainingActivity.query.filter_by(activity=request.form['recordActivity']).first()
        training_division = TrainingDivision.query.filter_by(division=request.form['recordDivision']).first()

        # set the new record datatype
        newrecord = Record()
        newrecord.date_start = date_start
        newrecord.date_finish = date_finish
        newrecord.date_expire = date_expire
        newrecord.title = request.form['recordTitle']
        newrecord.description = request.form['recordDescription']
        newrecord.notes = request.form['recordNotes']
        newrecord.training_provider = request.form['recordProvider']
        newrecord.training_location = request.form['recordLocation']
        newrecord.duration = duration.time()
        newrecord.duration_risk = time_risk.time()
        newrecord.duration_business = time_business.time()
        newrecord.duration_practice = time_aop.time()
        newrecord.training_type_id = training_type.id
        newrecord.training_activity_id = training_activity.id
        newrecord.training_division_id = training_division.id

        current_app.logger.debug(newrecord)

        # save data to DB
        db.session.add(newrecord)
        db.session.commit()
        # return to record page
        return redirect('/records')
    else:
        current_app.logger.debug("GET - no valid POST data")

        # get form values
        trg_activity = TrainingActivity.query.all()
        trg_type = TrainingType.query.all()
        trg_division = TrainingDivision.query.all()

        return render_template('record_add.html',
                               form=recordform,
                               trg_type=trg_type, trg_activity=trg_activity, trg_division=trg_division,
                               date_today=date_today)


@blueprint_records.route('/record/<record_id>')
def edit_record(record_id):
    record = Record.query.filter_by(id=record_id).first()
    return render_template('record_edit.html', record=record)
