Vagrant.configure("2") do |config|

    servers=[
      {
        :hostname => "Web1",
        :box => "ubuntu/bionic64",
        :ip => "172.16.1.50",
        :ssh_port => '2200'
      },
      {
        :hostname => "Web2",
        :box => "ubuntu/bionic64",
        :ip => "172.16.1.51",
        :ssh_port => '2201'
      },
      {
        :hostname => "WebLb",
        :box => "ubuntu/bionic64",
        :ip => "172.16.1.52",
        :ssh_port => '2202'
      }
    ]

    servers.each do |computer|
      config.vm.define computer[:hostname] do |node|
        node.vm.box = computer[:box]
        node.vm.hostname = computer[:hostname]
        node.vm.network :private_network, ip: computer[:ip]
        node.vm.network "forwarded_port", guest: 22, host: computer[:ssh_port], id: "ssh"
        #node.vm.synced_folder "../data", "/home/vagrant/data"
        #node.vm.provision "file", source: "./copiedfile.txt", destination: "/home/vagrant/copiedfile.txt"
        node.vm.provision "ansible" do |ansible|
            ansible.playbook = "main.yml"
        end
        
        node.vm.provider :virtualbox do |vb|
          vb.customize ["modifyvm", :id, "--memory", 1024]
          vb.customize ["modifyvm", :id, "--cpus", 2]
        end
      end
    end

  end
