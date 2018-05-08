### Log Analysis:
This project is Udacity Log Analysis project using sql commands and 
a python script to fetch the sql output using psycopg2 library.

### Setup:
Below steps need to be followed to create the database setup.

1. Install [Virtualbox](https://www.virtualbox.org) to host virtual machines.
2. Install [Vagrant](https://www.vagrantup.com) which can build and maintain
virtual machines through configuration files(Vagrant file).
3. Install [Gitbash](https://git-scm.com/downloads), which can be used as a
shell for running linux commands on windows. 
4. Clone or download [FullStackNanoDegreeVM](https://github.com/udacity/fullstack-nanodegree-vm) github project files.
The VagrantFile is present in the folder "vagrant". Use this configuration file for bringing up the desired virtual machine.

5. To download and power on the VM, Open Gitbash and cd into the folder
location where the vagrant file is downloaded and execute the below command to power on.

`vagrant up`

6. After powering on the VM Ssh into the virtual machine by using the 
below command.

`vagrant ssh`

7. Create a database called news. 

`psql`

`create database news;`

`<ctr><d>`

8. Download and Import the sql dump from the provided [SqlDump](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

`psql -d news -f newsdata.sql`

### To Run:
Execute the command using the below command.

`python log-analysis.py`
