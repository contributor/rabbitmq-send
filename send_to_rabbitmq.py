import pika
import os
import ssl
import certifi

def send_message(host, port, username, password, virtual_host, queue_name, message):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl_options = pika.SSLOptions(context=ssl_context)

    connection_params = pika.ConnectionParameters(
        host=host,
        port=port,
        credentials=pika.PlainCredentials(username, password),
        virtual_host=virtual_host,
        ssl_options=ssl_options
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    print(f" [x] Sent '{message}' to queue '{queue_name}'")

    connection.close()

if __name__ == "__main__":
    rabbitmq_host = os.getenv('RABBITMQ_HOST')
    rabbitmq_port = int(os.getenv('RABBITMQ_PORT'))
    rabbitmq_username = os.getenv('RABBITMQ_USERNAME')
    rabbitmq_password = os.getenv('RABBITMQ_PASSWORD')
    virtual_host = os.getenv('VIRTUAL_HOST')

    queue_name = os.getenv('QUEUE_NAME')
    message = os.getenv('MESSAGE')

    send_message(rabbitmq_host, rabbitmq_port, rabbitmq_username, rabbitmq_password, virtual_host, queue_name, message)
