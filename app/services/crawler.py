from typing import List, Tuple

from . import data, job_queue, url
from app import repositories as repo


def get_crawled_data(entered_url: str) -> str:
    data_id = url.get_data_id_from_enterd_url(entered_url)
    crawler_data = data.get_data_with_id(data_id)
    return crawler_data if crawler_data else \
        "You haven't request any crawler request with this url " + entered_url


def register_new_crawlers(urls: List[str]):
    job_queue.crawl_data_from_urls(urls)


# Return crawler data and true url of website
def crawl(url: str) -> Tuple[str, str]:
    return repo.crawler.crawl(url)
