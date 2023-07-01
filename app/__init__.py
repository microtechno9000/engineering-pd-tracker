from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialise Flask Extensions
    db.init_app(app)
    
    # Register blueprints here
    from app.main import blueprint_main
    from app.media import blueprint_media
    from app.records import blueprint_records
    from app.settings import blueprint_settings
    app.register_blueprint(blueprint_main)
    app.register_blueprint(blueprint_media)
    app.register_blueprint(blueprint_records)
    app.register_blueprint(blueprint_settings)

    return app
