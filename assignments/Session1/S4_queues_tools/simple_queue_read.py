import pika
import os

"""
@author : Steven Francony
@brief : a simple example of queue publishing or reading whether the argument -read is passed when calling the script
"""

counter = 0
amqp_url='amqp://itgfanyr:a63KOZk_gxLVV9TX2Gg9VG4ei5iHslX6@puma.rmq.cloudamqp.com/itgfanyr'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)

params = pika.URLParameters(url)
params.socket_timeout = 5


#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')


def callback(ch, method, properties, body):
	global counter
	counter += 1
	print(" [X] Received " + str(body))
	print("You received " + str(counter) + " message(s)")
	
channel.basic_consume(callback,
	queue='presentation',
	no_ack=True)

print(" [*] Waiting or messages. To exit press CTRL+C'")

channel.start_consuming()