# Return crawler data and true url of website
from typing import Tuple

import requests

from app import helpers


def crawl(entered_url: str) -> Tuple[str, str]:
    urls = helpers.url.get_urls(entered_url)
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text, response.url
        except:
            pass
    return "Can't get data from " + entered_url, entered_url
