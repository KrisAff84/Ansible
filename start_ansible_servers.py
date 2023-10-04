import boto3

region = 'us-west-2'

def start_ec2_fleet(node1, node2, node3):
    ec2 = boto3.client('ec2', region_name=region)
    waiter = ec2.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[node1, node2, node3])
    response = ec2.start_instances(
        InstanceIds=[
            node1,
            node2,
            node3
        ],
    )

def get_public_ips(node1, node2, node3, zshrc_file, line_number1, line_number2, line_number3, inv_file):
    print()
    print('Waiting for instances to start...')
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[node1, node2, node3])
    response = ec2.describe_instances(
        InstanceIds=[
            node1,
            node2,
            node3
        ],
    )
    print()
    new_ips = []
    idx = 0
    for instance in response['Reservations'][0]['Instances']:
        print(f"Public IP of Node {idx + 1}: {instance['PublicIpAddress']}")
        new_ips.append(instance['PublicIpAddress'])
        idx += 1

    with open(zshrc_file, 'r') as file:
        lines = file.readlines()

    lines[line_number1 - 1] = f'ANode1="ec2-user@{new_ips[0]}" \n'
    lines[line_number2 - 1] = f'ANode2="ec2-user@{new_ips[1]}" \n'
    lines[line_number3 - 1] = f'ANode3="ec2-user@{new_ips[2]}" \n'

    with open(zshrc_file, 'w') as file:
        file.writelines(lines)  

    with open(inv_file, 'r') as file:
        lines = file.readlines()
    
    lines[1] = f'ec2-user@{new_ips[0]} \n'
    lines[4] = f'ec2-user@{new_ips[1]} \n'
    lines[7] = f'ec2-user@{new_ips[2]} \n'

    with open(inv_file, 'w') as file:
        file.writelines(lines)

    print()
    print('New IPs of fleet successfully written to config file')
    print('To SSH into instances use "ssh <$ANode1, $ANode2, $ANode3>"')
    print()  


def main():
    node1 ='i-07b9bc7dc0994ce46'
    node2 ='i-0872672d57ec39b3a'
    node3 ='i-029242cf135dd859f'
    zshrc_file ='/Users/Kris/.zshrc'
    inv_file = 'inventory'
    line_number1 = 11
    line_number2 = 12
    line_number3 = 13
    start_ec2_fleet(node1, node2, node3)
    get_public_ips(node1, node2, node3, zshrc_file, line_number1, line_number2, line_number3, inv_file)


if __name__ == '__main__':
    main()
    