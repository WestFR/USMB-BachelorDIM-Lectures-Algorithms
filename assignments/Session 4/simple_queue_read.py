"""
@author : Steven FRANCONY
@brief : a simple example of queue reading
"""

import pika
import os

amqp_url='amqp://itgfanyr:a63KOZk_gxLVV9TX2Gg9VG4ei5iHslX6@puma.rmq.cloudamqp.com/itgfanyr'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='presentation')

def callback(ch, method, properties, body):
	print(" [X] Received %r" % body)


channel.basic_consume(callback, queue='presentation', no_ack=True)
print('[X] Waiting for messages. To exit press CTRL + C')

channel.start_consuming()