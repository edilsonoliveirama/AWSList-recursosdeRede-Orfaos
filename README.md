# AWS List Orphaned Resources

Este script em Python usa a biblioteca Boto3 para listar os recursos órfãos na sua conta AWS, incluindo security groups, subnets e VPCs que não estão associados a nenhuma instância EC2.

## Pré-requisitos

- Python 3 instalado
- Biblioteca Boto3 instalada (`pip install boto3`)
- Credenciais AWS configuradas (através de `~/.aws/credentials` ou variáveis de ambiente)

## Como usar

1. Faça o download do script `aws_list_orphaned_resources.py`.
2. Certifique-se de que você tem os pré-requisitos instalados e suas credenciais AWS configuradas.
3. Execute o script usando o Python 3:

    ```bash
    python3 aws_list_orphaned_resources.py
    ```

4. O script irá listar os security groups, subnets e VPCs órfãos na sua conta AWS, ou seja, aqueles que não estão associados a nenhuma instância EC2.

## Ajustando o script

Você pode ajustar o script conforme necessário para atender às suas necessidades. Por exemplo, você pode modificar o nível de logging, adicionar tratamento de erros adicional ou implementar funcionalidades adicionais de filtragem.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar este script.

## Licença

Este script é fornecido sob a [Licença MIT](LICENSE).
