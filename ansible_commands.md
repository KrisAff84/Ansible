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

# To run ansible playbook
ansible-playbook --ask-become-pass <file_name>     or
ansible-playbook -K <file_name>