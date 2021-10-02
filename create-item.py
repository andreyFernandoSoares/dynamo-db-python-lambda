import boto3

client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = client.Table("cinema")
    table.put_item(Item={'id': 1, 'nome': 'homem aranha', 'genero': 'acao e aventura', 'produtora': 'marvel'})
