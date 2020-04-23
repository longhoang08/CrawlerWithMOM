import flask_migrate
import flask_sqlalchemy
import flask_bcrypt

from dotenv import load_dotenv

from config import _DOT_ENV_PATH

load_dotenv(_DOT_ENV_PATH)

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate(db=db)
bcrypt = flask_bcrypt.Bcrypt()


def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)

from .base import TimestampMixin
from .data import Data