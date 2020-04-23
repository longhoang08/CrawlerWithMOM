from app import repositories
from app.models import Data
from . import url


def get_data_with_url(entered_url: str) -> str:
    if not entered_url: return None
    data = repositories.data.find_by_url(entered_url)
    return data.get_crawler_data() if data else None


def get_data_with_id(id: int) -> str:
    if not id: return None
    data = repositories.data.find_by_id(id)
    return data.get_crawler_data() if data else None


def create_or_update_crawler_data(entered_url: str, crawler_data: str, redirected_url: str) -> Data:
    data = repositories.data.find_by_url(redirected_url)
    if not data:
        data = repositories.data.save_data_to_database(
            url=redirected_url,
            crawler_data=crawler_data
        )
        url.create_or_update_url(repositories.data.find_by_url(redirected_url).id, entered_url)
        return data
    else:
        data.crawler_data = crawler_data
        repositories.data.save(data)
        url.create_or_update_url(data.id, entered_url)
        return data
