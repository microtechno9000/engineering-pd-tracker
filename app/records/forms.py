"""
Forms handler for records
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields import DateField


class NewRecord(FlaskForm):
    """
    New Record form
    """
    recordTitle = StringField('recordTitle', validators=[DataRequired()])
    recordProvider = StringField('recordProvider', validators=[DataRequired()])
    recordActivity = StringField('recordActivity', validators=[DataRequired()])
    recordStartDate = DateField('recordStartDate', format='%Y-%m-%d')
    recordFinishDate = DateField('recordFinishDate', format='%Y-%m-%d')
    recordDivision = StringField('recordDivision', validators=[DataRequired()])
    recordLocation = StringField('recordLocation', validators=[DataRequired()])
    recordType = StringField('recordType', validators=[DataRequired()])
    recordTimeRisk = IntegerField('recordTimeRisk', validators=[DataRequired()])
    recordTimeMgmt = IntegerField('recordTimeMgmt', validators=[DataRequired()])
    recordTimeAop = IntegerField('recordTimeAop', validators=[DataRequired()])
    recordDescription = StringField('recordDescription', validators=[DataRequired()])
    recordNotes = StringField('recordNotes', validators=[DataRequired()])
    submit = SubmitField('Submit')
