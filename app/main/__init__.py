from flask import Blueprint

blueprint_main = Blueprint('main', __name__,
                           template_folder='templates')

from app.main import routes     # noqa: E402
