from flask import Blueprint

blueprint_settings = Blueprint('settings', __name__,
                               template_folder='templates')

from app.settings import routes     # noqa: E402, F401
