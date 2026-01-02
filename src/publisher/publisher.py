import os
import json
import pika

from typing import Dict
from dotenv import load_dotenv

load_dotenv()


class RabbitMQPublisher:
    def __init__(self):
        self.__host = os.getenv("RABBITMQ_HOST")
        self.__port = os.getenv("RABBITMQ_PORT")
        self.__username = os.getenv("RABBITMQ_USER")
        self.__password = os.getenv("RABBITMQ_PASS")
        self.__exchange = os.getenv("RABBITMQ_EXCHANGE")
        self.__channel = self.__create_channel()


    def __create_channel(self) -> pika.BlockingConnection:
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel

    def send_message(self, body: Dict, routing_key : str = "") -> None:
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
