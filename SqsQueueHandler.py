import boto3

client = boto3.client('sqs', 'us-west-2')

client.create_queue(QueueName='TestSQS')

queues = client.list_queues(QueueNamePrefix='test_queue')
test_queue_url = 'https://sqs.us-west-2.amazonaws.com/410031578117/TestSQS'

msgArr = []

while True:
    messages = client.receive_message(QueueUrl=test_queue_url,
                                      MaxNumberOfMessages=10)
    if 'Messages' in messages:  # when the queue is exhausted, the response dict contains no 'Messages' key
        for message in messages['Messages']:  # 'Messages' is a list

            print(message['Body'])

            if message['Body'] not in msgArr:
                msgArr.append(message['Body'])

            client.delete_message(QueueUrl=test_queue_url,
                                  ReceiptHandle=message['ReceiptHandle'])