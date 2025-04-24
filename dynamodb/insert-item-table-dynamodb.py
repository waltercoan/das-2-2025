import boto3

# Inicializa o cliente do DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Altere a região, se necessário

# Lista de itens a serem inseridos
items = [
    {
        'cpf': {'S': '12345678901'},
        'nome': {'S': 'João Silva'},
        'clienteativo': {'S': 'true'}
    },
    {
        'cpf': {'S': '98765432100'},
        'nome': {'S': 'Maria Oliveira'},
        'clienteativo': {'S': 'false'}
    },
    {
        'cpf': {'S': '45678912345'},
        'nome': {'S': 'Carlos Souza'},
        'clienteativo': {'S': 'true'}
    }
]

# Insere os itens na tabela
for item in items:
    try:
        response = dynamodb.put_item(
            TableName='cliente',
            Item=item
        )
        print(f"Item inserido com sucesso: {item}")
    except Exception as e:
        print(f"Erro ao inserir o item {item}: {e}")


