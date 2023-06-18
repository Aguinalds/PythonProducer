#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port='32790'))
channel = connection.channel()

channel.queue_declare(queue='EnviarMensagem')

message = ' '.join(sys.argv[1:]) or "Chegou"
channel.basic_publish(exchange='', routing_key='EnviarMensagem', body=message)
print(" [x] Sent %r" % message)
connection.close()
