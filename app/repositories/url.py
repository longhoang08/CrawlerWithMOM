from app import models
from app.models import Url


def save_url_to_database(**kwargs) -> Url:
    url = Url(**kwargs)
    return save(url)


def save(url: Url) -> Url:
    models.db.session.add(url)
    models.db.session.commit()
    return url


def find_url_by_entered_url(entered_url: str) -> Url:
    url = Url.query.filter(
        Url.entered_url == entered_url
    ).first()
    return url or None
