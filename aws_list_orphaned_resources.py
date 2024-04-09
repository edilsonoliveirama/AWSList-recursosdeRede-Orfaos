import boto3
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração de formato de logging personalizado
formatter = logging.Formatter('%(levelname)s: %(message)s')
for handler in logging.root.handlers:
    handler.setFormatter(formatter)

def list_orphaned_resources(ec2_resource):
    orphaned_resources = {
        'security_groups': [],
        'subnets': [],
        'vpcs': []
    }

    # Obtém todas as instâncias EC2 na conta
    instances = ec2_resource.instances.all()
    associated_security_groups = set()
    associated_subnets = set()
    associated_vpcs = set()

    # Extrai os IDs dos security groups, subnets e VPCs associadas a instâncias EC2
    for instance in instances:
        for group in instance.security_groups:
            associated_security_groups.add(group['GroupId'])
        associated_subnets.add(instance.subnet_id)
        associated_vpcs.add(instance.vpc_id)

    # Obtém todos os security groups, subnets e VPCs na conta
    security_groups = list(ec2_resource.security_groups.all())
    subnets = list(ec2_resource.subnets.all())
    vpcs = list(ec2_resource.vpcs.all())

    # Verifica os security groups órfãos
    for group in security_groups:
        if group.id not in associated_security_groups:
            orphaned_resources['security_groups'].append(group)

    # Verifica as subnets órfãs
    for subnet in subnets:
        if subnet.id not in associated_subnets:
            orphaned_resources['subnets'].append(subnet)

    # Verifica as VPCs órfãs
    for vpc in vpcs:
        if vpc.id not in associated_vpcs:
            orphaned_resources['vpcs'].append(vpc)

    return orphaned_resources

def main():
    try:
        # Inicializa o cliente EC2 e recurso EC2
        ec2_resource = boto3.resource('ec2')

        orphaned_resources = list_orphaned_resources(ec2_resource)

        for resource_type, resources in orphaned_resources.items():
            if resources:
                logger.info(f"{resource_type.capitalize()} órfãos encontrados:")
                for resource in resources:
                    logger.info(f"ID: {resource.id}, Nome: {resource.id}")
            else:
                logger.info(f"Nenhum {resource_type} órfão encontrado.")
    except Exception as e:
        logger.error(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
