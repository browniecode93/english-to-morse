import pika, json

params = pika.URLParameters('amqps://tfhyafsd:AfCkvL237tDy1wlKfJeOJdRSoyBnuJ9G@fish.rmq.cloudamqp.com/tfhyafsd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='consumer')


def callback(ch, method, properties, body):
    print('Received in consumer')
    data = json.loads(body)
    print(data)


channel.basic_consume(queue='consumer', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()

channel.close()
