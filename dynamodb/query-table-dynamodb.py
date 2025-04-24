import boto3

# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Altere a região, se necessário

try:
    # Realiza uma query na tabela cliente com base no campo cpf
    response = dynamodb.query(
        TableName='cliente',
        KeyConditionExpression='cpf = :cpf',
        ExpressionAttributeValues={
            ':cpf': {'S': '12345678901'}  # Substitua pelo valor desejado
        }
    )

    if 'Items' in response and response['Items']:
        print("Itens encontrados:")
        for item in response['Items']:
            print(item)
    else:
        print("Nenhum item encontrado.")

except Exception as e:
    print("Erro ao realizar a query:", e)
