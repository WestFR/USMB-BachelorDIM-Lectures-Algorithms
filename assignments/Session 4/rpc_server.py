"""
@author: Steven Francony
@brief : Simple example of a remote procedure (server side)
"""

import pika
import os
import uuid
import msgpack
import msgpack_numpy as m
import numpy as np

# Connection paramaters
amqp_url='amqp://itgfanyr:a63KOZk_gxLVV9TX2Gg9VG4ei5iHslX6@puma.rmq.cloudamqp.com/itgfanyr'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# Init communication
connection = pika.BlockingConnection(params) 
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

# Function to process the message sent and reply to
def on_request(ch, method, props, body):
    
    decoded_message = msgpack.unpackb(str(body), object_hook = m.decode)
    print("Message received from client : " + decoded_message['value'])

    #response = "I'm fine"
    response = {"type":0, "value":"I'm fine !"}
    
    encoded_message = msgpack.packb(response, default = m.encode)
    print("Message sent to the client : " + response['value'])
    
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=encoded_message)
                    
    # Acknowledge
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Wait for request
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

# Display messages
print(" [X] Waiting or messages. To exit press CTRL+C'")
print(" [x] Awaiting RPC requests")

channel.start_consuming()