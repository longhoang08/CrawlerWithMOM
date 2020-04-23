import flask_restplus
from flask import request

from app.extensions import Namespace
from .schema import requests
from .. import services

ns = Namespace('cralwer', description='Crawler operations')


@ns.route('/get_data/<web_url>', methods=['GET'])
class GetCrawlData(flask_restplus.Resource):
    def get(self, web_url):
        return services.crawler.get_crawled_data(web_url)


_crawl_request = ns.model('crawl_req', requests.crawl_request)


@ns.route('/crawl', methods=['POST'])
class Crawler(flask_restplus.Resource):
    @ns.expect(_crawl_request)
    def post(self):
        data = request.args or request.json
        services.job_queue.crawl_data_from_urls(**data)
        return "OK"
