# installs and configures  Nginx server using Puppet manifest
package { 'nginx':
  ensure => installed,
}

file_line { 'dope':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me http://35.237.80.55//mazaodigi.html permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

