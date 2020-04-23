from app import models


def save_data_to_database(**kwargs) -> models.Data:
    user = models.Data(**kwargs)
    return save(user)


def save(data: models.Data) -> models.Data:
    models.db.session.add(data)
    models.db.session.commit()
    return data


def find_by_url(url: str) -> models.Data:
    data = models.Data.query.filter(
        models.Data.url == url
    ).first()

    return data or None


def find_by_id(id: int) -> models.Data:
    data = models.Data.query.filter(
        models.Data.id == id
    ).first()

    return data or None
