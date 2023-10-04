ansible all —list-hosts
ansible all -m gather_facts

# To install packages
ansible all -m yum -a name=<package_name> --become --ask-become-pass

# Install and update packages
ansible all -m yum -a "name=<package_name> state=latest" --become --ask-become-pass

# Install updates on each server
ansible all -m apt -a "upgrade=dist" --become --ask-become-pass

# To have task only run on specified distrubution, add to playbook under " - name"
when: ansible_distribution == "<distro>"

# Not an ansible command - to install EPEL for RHEL 9
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo dnf config-manager --set-enabled epel

# To run ansible playbook (Don't actually need --ask-become-pass or -K for EC2 instances)
ansible-playbook --ask-become-pass <file_name>     or
ansible-playbook -K <file_name>

# To list available tags
ansible-playbook --list-tags <file>

# To run tasks associated with specific tag
ansible-playbook --tags <tags> -K <file>

# To run tasks associated with multiple tags
ansible-playbook --tags "<tag>,<tag>" -K <file>

# When using copy module the src directory is assumed to be files
# No need to write "files" if the file to be copied is inside

# ********** Why can't I connect to local host ??? ####################
# Figured it out, see localsetup.yml for example of setting up on MacOS

# Use 'lineinfile' module for changing a line in a file

# Not an Ansible Command - to view public key material from AWS generated key
# From AWS CLI
aws ec2 describe-key-pairs --key-names <key_name> --include-public-key 

# From Private Key file
ssh-keygen -y -f <path_to_key>

# Not an Ansible Command - To generate key pair
ssh-keygen -t <type(rsa_or_ed25519)> -C "comment" 

# To use roles with Ansible you need directory called roles with subdirectory for each role and tasks

# roles/<role_name>/tasks/

# Under each task directory create main.yml to place tasks, no need for hosts topdown parameter