from app.models import kafka_producer
from config import KAFKA_TOPIC


def push_into_kafka(data: str):
    print('Pushing', data, 'to queue')
    url_bytes = bytes(data, encoding='utf-8')
    kafka_producer.send(KAFKA_TOPIC, value=url_bytes, key=url_bytes)
