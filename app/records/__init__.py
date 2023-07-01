from flask import Blueprint

blueprint_records = Blueprint('records', __name__,
                              template_folder='templates')

from app.records import routes  # noqa: E402
