# Install an especific version of flask (2.1.0)

package {'install_flask':
    name   => 'flask',
    ensure => '2.1.0',
    provider => pip3,
    command => '/usr/bin/pip3',
}
