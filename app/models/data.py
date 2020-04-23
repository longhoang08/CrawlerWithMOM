from app.models import db
from app.models.base import TimestampMixin


class Data(db.Model, TimestampMixin):
    """
    Contains information of data table
    """
    __tablename__ = 'data'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), unique=True)
    crawler_data = db.Column(db.Text, nullable=False, unique=False)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'url': self.url,
            'crawler_data': self.crawler_data,
        }

    def get_id(self) -> int:
        return self.id

    def get_crawler_data(self) -> str:
        return self.crawler_data
