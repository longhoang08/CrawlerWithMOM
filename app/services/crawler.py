from . import data


def get_crawled_data(url: str) -> str:
    crawler_data = data.get_data_with_url(url)
    return crawler_data if crawler_data else \
        "You haven't request any crawler request with this url " + url


def crawl(url: str) -> str:
    # TODO: crawl data from url
    return "mock_crawler_data"
