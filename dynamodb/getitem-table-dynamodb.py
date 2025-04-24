import boto3


# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Altere a região, se necessário

try:
    # Busca o item com o campo cpf igual a 45678912345
    response = dynamodb.get_item(
        TableName='cliente',
        Key={
            'cpf': {'S': '45678912345'}
        }
    )

    if 'Item' in response:
        print("Item encontrado:")
        print(response['Item'])
    else:
        print("Item não encontrado.")

except Exception as e:
    print("Erro ao buscar o item:", e)
