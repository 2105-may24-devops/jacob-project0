PUSHING PYTHON  
============
Project Description  
-------------------
A proof-of-concept implementation of a relational database is built programmatically by leveraging native data structures to mimic the behavior of an SQL database. Application testing, virtual environment configuration, and deployment to multiple virtual machines are automated. 

Technologies Used  
-----------------
- Python - version 3.9  
- Ansible - version 2.11.1  
- GNU Bash - version 4.4.20
- Git - version 2.17.1

Features  
-------
- Python:
  - OOP design
    - AssetManagementTable "is-a" KeyTable tailored for this use-case
    - KeyTable "is-a" Table that "has-a" Key as a auto-generated, unique primary key
    - Menu class is designed for easy usability in future projects
- DevOps:
  - Automated Testing via shell scripts and Ansible  
  - Automated deployment to multiple virtual machines via Ansible  
  - Automated provisioning of host environment with venv and installation of dependencies via Ansible

Getting Started  
---------------
*Prerequisites:*
- Bash
- Ansible
- Virtual machine with ssh credentials

Clone this repo: `git clone https://github.com/2105-may24-devops/jacob-project0.git`

Usage  
-----
1 - Open the YAML file named `inventory` and replace the values within <> as follows:
```YAML
all:
  <your-category>:
    hosts:
      <your-host-nickname-1>:
        ansible_host: <your-host-ip-address>
      <your-host-nickname-2>:
        ansible_host: <your-host-ip-address>
      <... more hosts if desired>
    vars:
      ansible_ssh_private_key_file: <your-ssh-key-file>.pem
      ansible_user: <your-user-name>
```

License  
-------
This project uses the following license: Free and Open Source.  
