import pika

params = pika.URLParameters('amqps://tfhyafsd:AfCkvL237tDy1wlKfJeOJdRSoyBnuJ9G@fish.rmq.cloudamqp.com/tfhyafsd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='consumer', body='hello')
