from flask import Blueprint

blueprint_media = Blueprint('media', __name__,
                            template_folder='templates')

from app.media import routes    # noqa: E402
