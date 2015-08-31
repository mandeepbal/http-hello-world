#!/bin/bash
yum install -y nginx
cat << EOF > /usr/share/nginx/html/index.html
Automation for the People
EOF
cat << EOF > /etc/nginx/conf.d/virtual.conf
server {
  listen 80;
  location / {
    root html;
    index index.html;
  }
}
EOF
service nginx start
