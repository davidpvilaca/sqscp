#!/usr/bin/env python

'''
This is an adaptation of a script obtained at: https://gist.github.com/Vidimensional/3394c11f2d73b7c29e6cf9509a1d50e0
'''

import json
import time
import argparse
import boto.sqs
from termcolor import cprint

parser = argparse.ArgumentParser(description="Migrate messages from SQS queues.")
parser.add_argument('-s', '--src', required=True,
                    help='Name of the source queue.')
parser.add_argument('-d', '--dst', required=True,
                    help='Name of the destination queue.')
parser.add_argument('--region', default='us-east-1',
                    help='The AWS region of the queues (default: \'us-east-1\').')
parser.add_argument('--remove', const=True, default=False,  action='store_const',
                    help='Remove messages after copy (default: False).')
args = parser.parse_args()

aws_region = args.region
src_queue_name = args.src
dst_queue_name = args.dst

conn = boto.sqs.connect_to_region(aws_region)

src_queue = conn.get_queue(src_queue_name)
dst_queue = conn.get_queue(dst_queue_name)
all_messages = []
messages = [None]

while len(messages) > 0:
  messages = src_queue.get_messages(10)
  all_messages = all_messages + messages
  for src_message in messages:
    dst_message = boto.sqs.message.RawMessage()
    print 'Processing message ' + src_message.id
    msg_body = src_message.get_body()
    dst_message.set_body(msg_body)
    dst_queue.write(dst_message)

if args.remove:
  for message in all_messages:
    src_queue.delete_message(message)
