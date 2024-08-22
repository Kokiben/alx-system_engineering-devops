# Increase the ULIMIT for Nginx
file_line { 'increase-nginx-ulimit':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT=4096',
  match => '^ULIMIT=',
  notify => Exec['nginx-restart'],
}

# Restart Nginx to apply the new settings
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/usr/local/bin:/bin:/sbin',
  refreshonly => true,
}

