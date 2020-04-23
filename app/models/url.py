from app.models import TimestampMixin, db


class Url(db.Model, TimestampMixin):
    __tablename__ = 'url'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_id = db.Column(db.Integer, nullable=False)
    entered_url = db.Column(db.String(255), unique=True)
