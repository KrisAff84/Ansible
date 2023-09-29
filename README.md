This repository is a collection of Ansible configuration files produced as I learn Ansible

All .yml files are configuration files.

ansible_commands.md contains some useful Ansible commands as well as general notes

In addition to the Ansible configuration files, the two files 'start_ansible_servers.py' and 'stop_ansible_servers.py' contain Python boto3 scripts for starting and stopping a fleet of EC2 instances. In addition to starting the servers, the start file will also re-write the IP addresses of the newly run instances into 'inventory' as well as the .zshrc file. Variables can then be used to SSH into the servers, removing the need to write out a different IP address every time. 
