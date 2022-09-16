# kills a process(killmenow)

exec {'pkill -f killmenow':
  path  =>  '/usr/bin/:/bin/:/usr/local/bin/'

}

