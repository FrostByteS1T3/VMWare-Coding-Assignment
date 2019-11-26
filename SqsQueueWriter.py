# VMWare Coding Assignment

import boto3

client = boto3.client('sqs', 'us-west-2')  # create client object

client.create_queue(QueueName='TestSQS')

queues = client.list_queues(QueueNamePrefix='test_queue')

test_queue_url = 'https://sqs.us-west-2.amazonaws.com/410031578117/TestSQS'

enqueue_response = client.send_message(QueueUrl=test_queue_url,
                                       MessageBody='This is a test message')

print('Message ID : ', enqueue_response['MessageId'])