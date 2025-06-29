# Design e Arquitetura de Software II

[AWS Canvas](https://awsacademy.instructure.com/courses/113113)

## Repositório dos alunos
- [Repos](https://gist.github.com/901f02fd5f852b62abab10b5fb2d6328.git)

## Aula 24/02
- Well-Architect Framework
  - Excelencia operacional
  - Segurança
  - Confiabilidade (Reliabillity)
  - Eficiência em performance
  - Otimização de custos
  - Sustentabilidade

## Aula 27/02
- Trade-Offs
  - Escalabilidade/Elasticidade
  - Automatização auto escalabilidade
  - Infraestrutura como Código
  - Tratar os recursos como descartaveis
  - Baixo acoplamento
  - Design de serviços e não servidores
  - Escolha o banco de dados correto

## Aula 06/03
- Trade-Offs
  - Evitar ponto único de falha
  - Otimização de custo
  - Use de cache
  - Proteger sua infraestrutura
- Infraestrutura global da AWS
  - Regiões
  - Zonas de Disponibilidade
  - Local Zones
  - Data Centers

## Aula 10/03
- Infraestrutura global da AWS
  - POPs - Edge Location
- Segurança
  - Modelo de responsabilidade compartilhado
  - Autenticação
  - Autorização
  - Princípio do privilégio mínimo
  - Criptografia

## Aula 13/03
- Modelo de responsabilidade compartilhada
- Princípio do privilégio mínimo
- Autenticação
- Autorização
- Identity and Access Management
- Usuários
- Acesso pela console / acesso programático

## Aula 17/03
- Policy de Identidade
- Policy de Recurso
- S3

## Aula 24/03
- S3 - Gerenciamento de ciclo de vida
- S3 - Versionamento
- S3 - CORS

```bash
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "http://127.0.0.1:5500"
        ],
        "ExposeHeaders": [
            "x-amz-server-side-encryption",
            "x-amz-request-id",
            "x-amz-id-2"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

## Aula 27/03
- Códigos S3

## Aula 31/03
- Códigos S3

## Aula 03/04
- Computing (EC2)
- EBS
- AMI

## Aula 07/04
- Placement (Cluster/Spread/Partition)
- EC2 Purchase model (on-demand/reserved/savings plans/spot)

## Aula 10/04
- RDS
- Bancos de dados relacionais
- Bancos de dados não relacionais

# Segundo Bimestre

## Aula 05/05
- VPC
- CIDR
- Subnet Pública

## Aula 12/05
- Fazer os laboratórios [Canvas](https://awsacademy.instructure.com/courses/113113)
- Guided lab: Creating a Virtual Private Cloud
- Challenge (Cafe) lab: Creating a VPC Networking Environment for the Café

## Aula 15/05
- Fazer os laboratórios [Canvas](https://awsacademy.instructure.com/courses/113113)
- Guided lab: Creating a Virtual Private Cloud
- Challenge (Cafe) lab: Creating a VPC Networking Environment for the Café

## Aula 19/05
- VPC Peering
- AWS VPN Site-to-Site
- AWS Direct Connect

## Aula 26/05
- IAM Groups
- Roles - AWS STS
- AWS Cognito

## Aula 29/05
- Criptografia simétrica
- Criptografia assimétrica

## Aula 09/06
- Fazer os laboratórios [Canvas](https://awsacademy.instructure.com/courses/113113)
- Guided lab: Creating a Highly Available Environment
- Challenge (Café) lab: Creating a Scalable and Highly Available Environment for the Café

## Aula 12/06
- Fazer os laboratórios [Canvas](https://awsacademy.instructure.com/courses/113113)
- Guided lab: Creating a Highly Available Environment
- Challenge (Café) lab: Creating a Scalable and Highly Available Environment for the Café

## Aula 16/06
- Load Balancer
- DNS

## Aula 23/06
- Infraestrutura como código

## Aula 26/06
- Como reduzir acoplamento das aplicações

############# FIM DO CONTEÚDO ##################

### Recuperação 30/06 e 03/07
- ENTREGA REPOSITÓRIOS 03/07
