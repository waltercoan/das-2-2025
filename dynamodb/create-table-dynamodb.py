import boto3

# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Altere a região, se necessário

try:
    # Criação da tabela
    response = dynamodb.create_table(
        TableName='cliente',
        KeySchema=[
            {
                'AttributeName': 'cpf',
                'KeyType': 'HASH'  # Chave de partição
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'cpf',
                'AttributeType': 'S'  # Tipo String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Tabela criada com sucesso!")
    print("Detalhes da tabela:", response)

except Exception as e:
    print("Erro ao criar a tabela:", e)

