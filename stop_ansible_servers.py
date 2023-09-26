import boto3
import json


def stop_ec2_instances(Instance1, Instance2, Instance3):
    ec2 = boto3.client('ec2')
    response = ec2.stop_instances(
        InstanceIds=[
            Instance1,
            Instance2,
            Instance3
        ]
    )
    print(json.dumps(response, indent=4, default=str))


def main():
    Instance1='i-07b9bc7dc0994ce46'
    Instance2='i-0872672d57ec39b3a'
    Instance3='i-029242cf135dd859f'
    stop_ec2_instances(Instance1, Instance2, Instance3)

if __name__ == '__main__':
    main()
    