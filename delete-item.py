import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = client.Table("cinema")
    response = table.delete_item(Key={'id': 1})
    print(response)
    
