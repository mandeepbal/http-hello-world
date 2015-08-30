#
# Cookbook Name:: http-hello-world
# Recipe:: default
#
# Copyright (C) 2015 Mandeep Bal
#
# All rights reserved - Do Not Redistribute
#

package 'httpd'

service 'httpd'
	action [:enable, :start]
end
