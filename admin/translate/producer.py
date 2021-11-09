import pika
import json

params = pika.URLParameters('amqps://tfhyafsd:AfCkvL237tDy1wlKfJeOJdRSoyBnuJ9G@fish.rmq.cloudamqp.com/tfhyafsd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(body):
    channel.basic_publish(exchange='', routing_key='consumer', body=json.dumps(body))
