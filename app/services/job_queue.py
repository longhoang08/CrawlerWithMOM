# add request to job queue to process
from typing import List

from kafka.admin import NewTopic

from . import data, crawler
from ..models import admin_client


def crawl_data_from_urls(urls: List[str]):
    # Add request to job queue
    for url in urls:
        data.create_or_update_crawler_data(url, crawler.crawl(url))
    return "DONE"


def create_topics():
    # example usage of kafka
    topic_list = []
    admin_client.create_topics(new_topics=topic_list, validate_only=False)