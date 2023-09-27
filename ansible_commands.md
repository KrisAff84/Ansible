ansible all —list-hosts
ansible all -m gather_facts

# To install packages
ansible all -m yum -a name=<package_name> --become --ask-become-pass

# Install and update packages
ansible all -m yum -a "name=<package_name> state=latest" --become --ask-become-pass

# Install updates on each server
ansible all -m apt -a "upgrade=dist" --become --ask-become-pass

# Not an ansible command - to install EPEL for RHEL 9
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo dnf config-manager --set-enabled epel