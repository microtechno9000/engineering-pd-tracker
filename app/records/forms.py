"""
Forms handler for records
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from wtforms.fields import DateField


class FormRecord(FlaskForm):
    """
    New Record form
    """
    title = StringField('Title', validators=[InputRequired()])
    training_provider = StringField('training_provider', validators=[InputRequired()])
    date_start = DateField('Training Start Date',
                           format='%Y-%m-%d', validators=[InputRequired()])
    date_finish = DateField('Training Finish Date',
                            format='%Y-%m-%d', validators=[InputRequired()])
    training_location = StringField('training_location', validators=[InputRequired()])
    duration_risk = StringField('duration_risk', validators=[InputRequired()])
    duration_business = StringField('duration_business', validators=[InputRequired()])
    duration_practice = StringField('duration_practice', validators=[InputRequired()])
    description = TextAreaField('Training Description')
    notes = TextAreaField('Training Notes')
    training_activity_id = SelectField("Select an Activity", coerce=str)
    training_type_id = SelectField("Select a Type", coerce=str)
    training_division_id = SelectField("Select an EA Division", coerce=str)

    submit = SubmitField('Submit')
