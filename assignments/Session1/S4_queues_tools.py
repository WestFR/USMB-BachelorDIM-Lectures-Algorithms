import pika
import os


amqp_url='amqp://itgfanyr:a63KOZk_gxLVV9TX2Gg9VG4ei5iHslX6@puma.rmq.cloudamqp.com/itgfanyr:1883'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)

params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.exchange_declare(exchange="presentation", exchange_type="direct",
                         passive=False, durable=True, auto_delete=False)

print("Sending message to create a queue")
channel.basic_publish('presentation', 'standard_key', 'queue:group',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))

connection.sleep(5)

"""" print("Sending text message to group")
channel.basic_publish('test_exchange', 'group_key', 'Message to group_key',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))

connection.sleep(5)

print("Sending text message")
channel.basic_publish('test_exchange', 'standard_key', 'Message to standard_key',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))
"""
connection.close()
