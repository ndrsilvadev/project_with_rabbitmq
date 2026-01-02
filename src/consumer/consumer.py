import os
import logging
import pika

from dotenv import load_dotenv

load_dotenv()

log = logging.getLogger(__name__)


class RabbitMQConsumer:
    def __init__(self, callback) -> None:
        self.__host = os.getenv("RABBITMQ_HOST")
        self.__port = os.getenv("RABBITMQ_PORT")
        self.__username = os.getenv("RABBITMQ_USER")
        self.__password = os.getenv("RABBITMQ_PASS")
        self.__queue = os.getenv("RABBITMQ_QUEUE")
        self.__callback = callback
        self.__create_channel()

    def __create_channel(self) -> None:
        # Establishes the connection with RabbitMQ
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        # Configures the queue
        self.__channel = pika.BlockingConnection(connection_parameters).channel()
        self.__channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        # Configures the queue consumer
        self.__channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

    def start(self) -> None:
        log.info(f"Listen RabbitMQ on Port {self.__port}")
        self.__channel.start_consuming()
