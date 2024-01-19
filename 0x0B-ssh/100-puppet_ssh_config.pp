# Changing the configuration file of the ssh again

augeas {'ssh_config_changes':
    context => '/files/etc/ssh/ssh_config/Host',
    changes => [
        'set PasswordAuthentication no',
        'set IdentityFile ~/.ssh/school',
    ],
}