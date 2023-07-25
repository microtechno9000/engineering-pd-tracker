from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_migrate import Migrate

# setup the database
db = SQLAlchemy()

# setup Flask Alembic
alembic = Alembic()

migrate = Migrate()
