import os
from alembic.script import ScriptDirectory
from alembic.config import Config  # noqa: F811
import sqlite3
import flask_migrate


def check_init(app):
    if check_database(app):
        if not check_database_current(app):
            update_database(app)
    else:
        # create db file
        # logger output doing things
        create_database(app)


def check_database(app):
    """
    Check if the database exists
    """
    file_db = app.config.get('SQLALCHEMY_DATABASE_URI')
    return os.path.isfile(file_db)


def check_database_current(app):
    """
    Check if the database is current
    """
    alembic_dir = app.config.get('migrations')
    file_db = app.config.get('SQLALCHEMY_DATABASE_URI')

    config = Config()
    config.set_main_option("script_location", alembic_dir)
    script = ScriptDirectory.from_config(config)

    head_revision = script.get_current_head()
    app.logger.debug("Alembic Head is: " + head_revision)

    conn = sqlite3.connect(file_db)
    db_c = conn.cursor()
    db_c.execute('SELECT version_num FROM alembic_version')
    db_version = db_c.fetchone()[0]
    app.logger.debug(f"Database version is: {db_version}")

    if head_revision == db_version:
        return True
    else:
        return False


def create_database(app):
    """
    Create database if not present
    """
    alembic_dir = app.config.get('migrations')
    with app.app_context():
        flask_migrate.upgrade(alembic_dir)


def update_database(app):
    """
    Update DB if not current
    """
    alembic_dir = app.config.get('migrations')
    with app.app_context():
        flask_migrate.upgrade(alembic_dir)
