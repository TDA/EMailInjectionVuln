#!/usr/bin/env python

import ConfigParser
import os.path
import pika
import crawler_pb2
import unicodedata

import logging
logging.basicConfig(level=logging.CRITICAL)


def _load_config_file():
    config = ConfigParser.SafeConfigParser()
    config_file = os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                                "config.cfg"))
    config.read(config_file)
    return config

def add_callback(callback):
    ''' Attaches a callback to the rabbitmq listener '''
    config = _load_config_file()
    creds = pika.PlainCredentials(
            username=config.get('rabbitmq', 'username'),
            password=config.get('rabbitmq', 'password'))
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            credentials=creds,
            host=config.get('rabbitmq', 'host'),
            virtual_host=config.get('rabbitmq', 'virtual_host')))
    channel = connection.channel()
    channel.exchange_declare(
            exchange=config.get('rabbitmq', 'exchange'),
            type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(
            exchange=config.get('rabbitmq', 'exchange'),
            queue=queue_name)

    def callback_wrapper(ch, method, properties, body):
        crawled_url = crawler_pb2.URL()
        if type(body) == unicode:
            body = unicodedata.normalize('NFKD', body).encode('ascii',
                                                              'ignore')
        try:
            crawled_url.ParseFromString(body)
        except:
            return
        callback(crawled_url)

    channel.basic_consume(callback_wrapper,
            queue=queue_name,
            no_ack=True)
    print ('Connected, waiting for urls...')
    channel.start_consuming()
