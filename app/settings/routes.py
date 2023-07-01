from flask import render_template

from app.settings import blueprint_settings


@blueprint_settings.route('/settings')
def media():
    return render_template('settings.html')
