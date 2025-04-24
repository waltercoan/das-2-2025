import boto3
# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Altere a região, se necessário

try:
    # Realiza um scan na tabela cliente com filtro no campo clienteativo
    response = dynamodb.scan(
        TableName='cliente',
        FilterExpression="clienteativo = :val",
        ExpressionAttributeValues={
            ':val': {'S': 'true'}
        }
    )

    if 'Items' in response and response['Items']:
        print("Itens encontrados com clienteativo = true:")
        for item in response['Items']:
            print(item)
    else:
        print("Nenhum item encontrado com clienteativo = true.")

except Exception as e:
    print("Erro ao realizar o scan:", e)
