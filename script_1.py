

#!/usr/bin/env python
# Encoding: utf-8

import os
import io
import stat
import sys

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

pkg_name = "isc-dhcp-server"

os.system('apt-get install -y isc-dhcp-server')

path_file = '/etc/dhcp/dhcpd.conf'

with open(path_file, 'r') as file:
    data = file.readlines()


data[23] = 'authoritative;\n'

data[27] = 'log-facility local7;\n'

data[52] = 'subnet 10.5.5.0 netmask 255.255.255.224 {\n'

data[53] = 'range 172.16.0.2 172.16.0.5;\n'

data[56] = 'option subnet-mask 255.255.255.0;\n'

data[58] = 'option broadcast-address 10.5.5.31;\n'

data[59] = 'default-lease-time 86400;\n'

data[60] = 'max-lease-time 7200;\n'

data[61] = '}\n'

with open(path_file, 'w') as file:
    file.writelines(data)
