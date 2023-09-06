from flask import Blueprint

blueprint_about = Blueprint('about', __name__,
                            template_folder='templates')

from app.about import routes  # noqa: E402, F401
