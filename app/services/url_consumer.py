from kafka import KafkaConsumer

from config import KAFKA_URL, CLIENT_ID, KAFKA_TOPIC
from . import data, crawler


def listen():
    consumer = KafkaConsumer(KAFKA_TOPIC,
                             bootstrap_servers=KAFKA_URL,
                             client_id=CLIENT_ID)

    for msg in consumer:
        url = msg.value.decode("utf-8")
        print('fucking bitch', url)
        data.create_or_update_crawler_data(url, *crawler.crawl(url))
