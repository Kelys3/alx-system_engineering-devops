# Correcting the stack to send out all requests with no errors.

exec {'replace':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before  => Exec['restart'],
}

exec {'restart':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo service nginx restart',
}
