from typing import List
import urllib.parse

HTTP = 'http'
HTTPS = 'https'
WWW = 'www.'


def get_url_with_protocol(url: str, protocol: str = HTTPS) -> str:
    url_parse = urllib.parse.urlparse(url, protocol)
    netloc = url_parse.netloc or url_parse.path
    path = url_parse.path if url_parse.netloc else ''
    if not netloc.startswith(WWW):
        netloc = WWW + netloc
    url_parse = urllib.parse.ParseResult(protocol, netloc, path, *url_parse[3:])
    return url_parse.geturl()


def get_urls(url: str) -> List[str]:
    return [get_url_with_protocol(url, HTTPS),
            get_url_with_protocol(url, HTTP)]
