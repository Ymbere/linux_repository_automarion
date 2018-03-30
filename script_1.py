

#!/usr/bin/env python
# Encoding: utf-8

import os
import io
import stat
import sys

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

os.system('apt-get install -y isc-dhcp-server')

path_file = '/etc/dhcp/dhcpd.conf'

with open(path_file, 'r') as file:
    data = file.readlines()


data[23] = 'authoritative;\n'

data[27] = 'log-facility local7;\n'

data[52] = 'subnet 172.16.0.0 netmask 255.255.255.0 {\n'

data[53] = ' range 172.16.0.2 172.16.0.50;\n'

data[56] = ' option subnet-mask 255.255.255.0;\n'

data[58] = ' option broadcast-address 172.16.0.255;\n'

data[59] = ' default-lease-time 86400;\n'

data[60] = ' max-lease-time 604800;\n'

data[61] = '}\n'

with open(path_file, 'w') as file:
    file.writelines(data)

path_file_2 = '/etc/default/isc-dhcp-server'

test = 'enp0s3'

with open(path_file_2, 'r') as file:
    data = file.readlines()

data[16] = 'INTERFACES="enp0s3"\n'

with open(path_file_2, 'w') as file:
    file.writelines(data)

path_file_3 = '/etc/network/interfaces'

with open(path_file_3, 'r') as file:
    data = file.readlines()

data[11] = '#iface enp0s3 inet dhcp\n'

new_lines = """iface enp0s3 inet static\n
address 172.16.0.1\n
network 172.16.0.0/24\n
netmask 255.255.255.0\n
broadcast 172.16.0.255\n"""

with open(path_file_3, 'w') as file:
    file.writelines(data)
    file.writelines(new_lines)
