from flask import render_template

from app.main import blueprint_main


@blueprint_main.route('/')
def index():
    return render_template('index.html')
