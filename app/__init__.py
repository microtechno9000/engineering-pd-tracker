from flask import Flask

from config import Config
from app.extensions import db
from app.extensions import migrate
from app.dbmanager import check_init
from app.extensions import csrf
from app.logs import setuplog


def create_app(config_class=Config):
    # Configure flask logger
    # noinspection PyUnusedLocal,PyPep8Naming
    dictConfig = setuplog(config_class)

    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)
    csrf.init_app(app)

    # Initialise Flask Extensions
    db.init_app(app)
    # alembic.init_app(app)
    migrate.init_app(app, db)

    # check database is current
    check_init(app)

    # Register blueprints here
    app.logger.debug("Loading blueprints")
    from app.main import blueprint_main
    from app.media import blueprint_media
    from app.records import blueprint_records
    from app.settings import blueprint_settings
    app.register_blueprint(blueprint_main)
    app.register_blueprint(blueprint_media)
    app.register_blueprint(blueprint_records)
    app.register_blueprint(blueprint_settings)

    return app
