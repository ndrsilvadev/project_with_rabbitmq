import logging

from core import setup_logging
from src.consumer import RabbitMQConsumer

setup_logging()
log = logging.getLogger(__name__)


if __name__ == "__main__":
    def callback(ch, method, properties, body) -> None:
        log.info(body)

    consumer: RabbitMQConsumer = RabbitMQConsumer(callback=callback)
    consumer.start()