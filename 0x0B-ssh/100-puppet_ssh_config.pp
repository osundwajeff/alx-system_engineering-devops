# client configuration using puppet
exec { 'Turn off passwd auth':
  command => 'bash -c "echo PasswordAuthentification no >> /etc/ssh/ssh_config"',
  path    => 'usr/bin:/usr/sbin:/bin'
}
exec { 'Declare identity file':
  command => 'bash -c "echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_congig"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
exec { 'Turn on pubkey auth':
  command => 'bash -c "echo PubkeyAuthentification yes >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
