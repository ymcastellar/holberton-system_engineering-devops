# create a file in /tmp

file { '/tmp/holberton':
ensure  => 'present',
path    => '/tmp/holberton',
node    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
