import pika


class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue_3"
        self.__callback = callback
        self.__channel = self.__create_channel()


    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(

            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(

                username=self.__username,
                password=self.__password
            )
        )


        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(

            queue=self.__queue,
            durable=True,
            arguments={
                
                "x-overflow": "reject-publish"
            }
        )


        channel.basic_consume(

            queue="data_queue",
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel


    def start(self):
        print(f'Listen RabbitMQ on port 5672')
        self.__channel.start_consuming()


def my_callback(ch, method, properties, body):
    print(body)


rabbitmq_consumer = RabbitmqConsumer(my_callback)
rabbitmq_consumer.start()