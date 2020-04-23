from typing import List

from . import data, job_queue


def get_crawled_data(url: str) -> str:
    crawler_data = data.get_data_with_url(url)
    return crawler_data if crawler_data else \
        "You haven't request any crawler request with this url " + url


def register_new_crawlers(urls: List[str]):
    job_queue.crawl_data_from_urls(urls)


def crawl(url: str) -> str:
    # TODO: crawl data from url
    return "mock_crawler_data"
