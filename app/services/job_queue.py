# add request to job queue to process
from typing import List

from . import data, crawler


def crawl_data_from_urls(urls: List[str]):
    # Add request to job queue
    for url in urls:
        data.create_or_update_crawler_data(url, crawler.crawl(url))
    return "DONE"
