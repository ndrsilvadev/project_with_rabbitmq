import logging

from typing import Dict
from core import setup_logging
from src.publisher import RabbitMQPublisher

setup_logging()
log = logging.getLogger(__name__)


if __name__ == "__main__":
    publisher: RabbitMQPublisher = RabbitMQPublisher()
    list_dict: list[Dict[str, str]] = [
        {"message": "Goog morning!"},
        {"message": "Hi, Michael!"},
        {"message": "How are you?"},
    ]

    for item in list_dict:
        publisher.send_message(item)
