"""
Forms handler for records
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from wtforms.fields import DateField


class FormRecord(FlaskForm):
    """
    New Record form
    """
    recordTitle = StringField('recordTitle', validators=[InputRequired()])
    recordProvider = StringField('recordProvider', validators=[InputRequired()])
    recordActivity = StringField('recordActivity', validators=[InputRequired()])
    recordStartDate = DateField('recordStartDate', format='%Y-%m-%d', validators=[InputRequired()])
    recordFinishDate = DateField('recordFinishDate', format='%Y-%m-%d', validators=[InputRequired()])
    recordDivision = StringField('recordDivision', validators=[InputRequired()])
    recordLocation = StringField('recordLocation', validators=[InputRequired()])
    recordType = StringField('recordType', validators=[InputRequired()])
    recordTimeRisk = StringField('recordTimeRisk', validators=[InputRequired()])
    recordTimeMgmt = StringField('recordTimeMgmt', validators=[InputRequired()])
    recordTimeAop = StringField('recordTimeAop', validators=[InputRequired()])
    recordDescription = StringField('recordDescription', validators=[InputRequired()])
    recordNotes = StringField('recordNotes', validators=[InputRequired()])
    submit = SubmitField('Submit')
