# set up  client SSH configuration file so that connection to the server is without typing a password.

file_line{
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '    PassworAuthentication no',
  replace =>  'true',
}
file_line{
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '    IdentityFile ~/.ssh/school',
  replace =>  'true',
}

