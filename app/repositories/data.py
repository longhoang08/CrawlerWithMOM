from app import models


def save_data_to_database(**kwargs) -> models.Data:
    user = models.Data(**kwargs)
    models.db.session.add(user)
    return user


def update_existed_data(data: models.Data) -> models.Data:
    models.db.session.add(data)
    return data


def find_by_url(url: str) -> models.Data:
    data = models.Data.query.filter(
        models.Data.url == url
    ).first()

    return data or None
