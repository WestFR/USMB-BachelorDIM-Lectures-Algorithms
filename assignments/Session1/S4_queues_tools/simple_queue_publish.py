import pika
import os

"""
@author : Steven Francony
@brief : a simple example of queue publishing
"""

amqp_url='amqp://itgfanyr:a63KOZk_gxLVV9TX2Gg9VG4ei5iHslX6@puma.rmq.cloudamqp.com/itgfanyr'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)

params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue="presentation")
channel.basic_publish(exchange='', routing_key='presentation', body='Hello itgfanyr !')

connection.close()

