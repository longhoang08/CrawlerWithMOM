from .. import repositories as repo
from ..models import Url


def create_or_update_url(data_id: int, entered_url: str) -> Url:
    url = repo.url.find_url_by_entered_url(entered_url)
    if url:
        url.data_id = data_id
        return repo.url.save(url)
    return repo.url.save_url_to_database(data_id=data_id, entered_url=entered_url)


def get_data_id_from_enterd_url(enterd_url: str) -> int:
    url = repo.url.find_url_by_entered_url(enterd_url)
    return url.data_id if url else None
