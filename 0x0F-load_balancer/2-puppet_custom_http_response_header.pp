# puppet manifest creating a custom HTTP header response
exec { '/usr/bin/env apt-get -y update':}
-> package { 'nginx':
  ensure => installed,
}

file_line { 'redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=Qpou6mFtV7o permanent;',
  require => Package['nginx'],
}

file_line { 'header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
