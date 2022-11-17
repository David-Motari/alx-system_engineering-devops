# A puppet script that enables the user holberton to login and open files without error
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
