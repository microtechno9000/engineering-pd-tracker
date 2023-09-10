from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

# Set up the database
db = SQLAlchemy()

# setup Flask Alembic
alembic = Alembic()

migrate = Migrate()

csrf = CSRFProtect()
