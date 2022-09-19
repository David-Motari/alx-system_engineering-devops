# set up  client SSH configuration file so that connection to the server is without typing a password.

file_line { 'Remove password auth':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '    PasswordAuthentication no',
  replace =>  true,
}

file_line { 'Change identity file':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '    IdentityFile ~/.ssh/school',
  replace =>  true,
}

