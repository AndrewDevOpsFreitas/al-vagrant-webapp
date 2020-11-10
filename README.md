# al-vagrant-webapp
AutomationLogic - Vagrant file creates 2 web servers served by an nginx loadbalancer.

Prequisites:

(Git)
Have git bash installed - see https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/

(Virtualbox)
Install virtualbox for your os - see https://www.virtualbox.org/wiki/Downloads
Default provider for vagrant machines, no configuration required

(Vagrant)
Install Vagrant - see https://www.vagrantup.com/downloads
Run "$vagrant version" to ensure that it is has installed correctly

Steps:

1. Clone the repo
Run "$git clone https://github.com/AndrewDevOpsFreitas/al-vagrant-webapp.git"

2. cd into project 
Run "$cd ${PATH_TO_PROJECT}/al-vagrant-webapp"

3. Run "$vagrant up", this needs to be in the same location as the Vagrantfile. Running first time will take some time for vagrant to fetch the boxes from the internet (around 5-10mins). This will create 4 machines: ansible-control, Web1, Web2, WebLb

4. Run "$vagrant ssh ansible-control" to connect to the ansible machine

5. Run "$ssh-keygen -t rsa -b 2048" to create a new ssh keypair to allow ssh connection between ansible host and stack, accept all command defaults.

6. Copy the contents of ~/.ssh/id_rsa.pub from ansible-control host, and paste in ~/.ssh/authorized_keys for the stack [Web1, Web2, WebLb].

7. Connect back to ansible-control. 
First check that at this point you can ssh to all machines from ansible-control "$ssh vagrant@Web1", "$ssh vagrant@Web2", "$ssh vagrant@WebLb" - say "yes" to any prompts 
Run "$ansible-playbook -i /vagrant/ansible/inventory/hosts /vagrant/ansible/deploy.yml"

8. Open a browser on your local machine, and search for 
http://172.16.1.53
If the loadbalancer isn't working, try going onto the web servers themselves at http://172.16.1.51:8000 or 
http://172.16.1.52:8000
