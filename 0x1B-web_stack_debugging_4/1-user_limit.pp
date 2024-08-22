#Change the OS configuration so that it is possible to login
file { 'lognFle':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#File erased'
}
