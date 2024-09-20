import os
import pika
from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):
    def __init__(self, exchange_name: str, queue_name: str, binding_key: str ) -> None:
        self.exchange_name = exchange_name
        self.binding_key = binding_key
        self.queue_name = queue_name
        self.setupRMQConnection()

    def setupRMQConnection(self)-> None:
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)

        channel = connection.channel()
        self.channel = channel
        channel.queue_declare(queue= self.queue_name)
        exchange = channel.exchange_declare(exchange= self.exchange_name)

        channel.queue_bind(
        queue= self.queue_name,
        routing_key= self.binding_key,
        exchange=self.exchange_name,
        )

    def onMessageCallback(self) -> None:
        message = json.loads(JsonMessageObject)
        self.channel.basic_ack(method_frame.delivery_tag, False)

    def startConsuming(self)->None:
        self.channel.start_consuming()



