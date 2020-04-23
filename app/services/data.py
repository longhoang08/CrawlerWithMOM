from app import repositories
from app.models import Data


def get_data_with_url(url: str) -> str:
    data = repositories.data.find_by_url(url)
    return data.get_crawler_data() if data else None


def create_or_update_crawler_data(url: str, crawler_data: str) -> Data:
    data = repositories.data.find_by_url(url)
    if not data:
        return repositories.data.save_data_to_database(
            url=url,
            crawler_data=crawler_data
        )
    else:
        data.crawler_data = crawler_data
        return repositories.data.update_existed_data(data)
