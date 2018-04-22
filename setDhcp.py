
# !/usr/bin/env python
# Encoding: utf-8

import os

import system.system_operations

s = system.system_operations

os.system('apt-get install -y isc-dhcp-server')

path_file = '/etc/dhcp/dhcpd.conf'

with open(path_file, 'r') as file:
    data = file.readlines()

data[s.get_line_number('#authoritative;', path_file)] = 'authoritative;\n'

data[s.get_line_number('#authoritative;', path_file).get_line_number('#subnet 10.5.5.0 netmask 255.255.255.224 {',
                                                                     path_file)] = \
    'subnet 172.16.0.0 netmask 255.255.255.0 {\n'

data[s.get_line_number('#  range 10.5.5.26 10.5.5.30;', path_file)] = '  range 172.16.0.2 172.16.0.50;\n'

data[56] = ' option subnet-mask 255.255.255.0;\n'

data[s.get_line_number('#  option broadcast-address 10.5.5.31;', path_file)] = \
    '  option broadcast-address 172.16.0.255;\n'

data[s.get_line_number('#  default-lease-time 600;', path_file)] = '  default-lease-time 86400;\n'

data[s.get_line_number('#  max-lease-time 7200;', path_file)] = '  max-lease-time 604800;\n'

data[s.get_line_number('#  max-lease-time 7200;', path_file) + 1] = '}'

s.write_file(path_file, data)

os.system('dhcpd -t')

path_file = '/etc/default/isc-dhcp-server'

with open(path_file, 'r') as file:
    data = file.readlines()

data[SystemOperations.get_line_number('INTERFACES=""', path_file)] = 'INTERFACES="eth0"'

s.write_file(path_file, data)

path_file = '/etc/network/interfaces'

with open(path_file, 'r') as file:
    data = file.readlines()

data[s.get_line_number('iface eth0 inet dhcp', path_file)] = '#iface eth0 inet dhcp'

new_lines = """iface eth0 inet static\n
address 172.16.0.1\n
network 172.16.0.0/24\n
netmask 255.255.255.0\n
broadcast 172.16.0.255\n"""

s.write_file(path_file, data)

s.write_file(path_file, new_lines)
