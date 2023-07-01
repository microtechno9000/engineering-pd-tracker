from flask import render_template

from app.media import blueprint_media


@blueprint_media.route('/media')
def media():
    return render_template('media.html')
