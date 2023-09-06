from flask import render_template

from app.about import blueprint_about


@blueprint_about.route('/about')
def index():
    return render_template('about.html')
