# strace can attach to a current running process
# Apache is returning a 500 error.

exec { 'Fixer_u':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  onlyif  => "grep 'phpp' /var/www/html/wp-settings.php",
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}
