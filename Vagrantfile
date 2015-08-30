# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = '2'
Vagrant.require_version '>= 1.5.0'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.hostname = 'http-hello-world-berkshelf'
  config.vm.box = 'chef/centos-6.6'
  config.vm.box_url = 'http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_centos-6.6_chef-provisionerless.box'
  config.omnibus.chef_version = :latest
  config.vm.network :private_network, ip: '10.0.0.1'
  config.vm.boot_timeout = 120
  config.berkshelf.enabled = true

  config.vm.provision :chef_solo do |chef|
    chef.data_bags_path = 'data_bags'
    chef.run_list = [
      'recipe[http-hello-world::default]'
    ]
  end
end

