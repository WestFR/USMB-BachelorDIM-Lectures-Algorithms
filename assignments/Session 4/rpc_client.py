"""
Created on Tue Oct 24 09:22:58 2017
@author: Steven Francony
@brief : Simple example of a remote procedure (client side)
"""

import pika
import os
import uuid
import msgpack
import msgpack_numpy as m
import numpy as np #if Numpy is required.

# Connection paramaters
amqp_url='amqp://itgfanyr:a63KOZk_gxLVV9TX2Gg9VG4ei5iHslX6@puma.rmq.cloudamqp.com/itgfanyr'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# Init variables
callback_queue='rpc_queue'
message={"type":0, "value":"hi, how fine?"}
encoded_message = msgpack.packb(message, default = m.encode)

class RpcClient(object):
    def __init__(self):        
        self.connection = pika.BlockingConnection(params) 
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
            decoded_response = msgpack.unpackb(str(self.response), object_hook = m.decode)
            print(decoded_response['value'])

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=encoded_message)
                                   #message
                                   
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)

rpc = RpcClient()

response = rpc.call(encoded_message)

print(" [x] Requesting")
print(" [.] Server :" + response)