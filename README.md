# RabbitMQ Notifier Action

This GitHub Action sends a message to a RabbitMQ queue.

## Inputs

| Name           | Description              | Required | Default |
|----------------|--------------------------|----------|---------|
| `rabbitmq_host` | The RabbitMQ host         | true     |         |
| `rabbitmq_port` | The RabbitMQ port         | false    | 5672    |
| `queue_name`    | The RabbitMQ queue name   | true     |         |
| `message`       | The message to send       | true     |         |

## Example Workflow

```yaml
jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Send message to RabbitMQ
        uses: username, password
        with:
          rabbitmq_host: ${{ secrets.RABBITMQ_HOST }}  # Secret for RabbitMQ host
          rabbitmq_port: 5671  # Default AMQPS port
          virtual_host: ${{ secrets.RABBITMQ_VIRTUAL_HOST }}  # Secret for RabbitMQ virtual host
          queue_name: your-queue-name  # Replace with your RabbitMQ queue name
          message: 'A new commit has been pushed!'  # Customize the message
          rabbitmq_username: ${{ secrets.RABBITMQ_USERNAME }}  # Secret for RabbitMQ username
          rabbitmq_password: ${{ secrets.RABBITMQ_PASSWORD }}  # Secret for RabbitMQ password

