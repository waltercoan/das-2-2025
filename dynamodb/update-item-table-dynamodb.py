import boto3

# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Altere a região, se necessário

try:
    # Atualiza o campo clienteativo do cliente Maria
    response = dynamodb.update_item(
        TableName='cliente',
        Key={
            'cpf': {'S': '98765432100'}  # CPF do cliente Maria
        },
        UpdateExpression="SET clienteativo = :val",
        ExpressionAttributeValues={
            ':val': {'S': 'true'}
        },
        ReturnValues="UPDATED_NEW"
    )

    print("Item atualizado com sucesso!")
    print("Detalhes da atualização:", response)

except Exception as e:
    print("Erro ao atualizar o item:", e)
