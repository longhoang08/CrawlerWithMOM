import flask_migrate
import flask_sqlalchemy
import flask_bcrypt

from dotenv import load_dotenv
from kafka import KafkaAdminClient, KafkaProducer

from config import _DOT_ENV_PATH, KAFKA_URL, CLIENT_ID

load_dotenv(_DOT_ENV_PATH)

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate(db=db)
bcrypt = flask_bcrypt.Bcrypt()
admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_URL,
    client_id=CLIENT_ID)
kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_URL,
                               client_id=CLIENT_ID)


def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)


from .base import TimestampMixin
from .data import Data
from .url import Url
