# !/usr/bin/env python
# Encoding: utf-8

import os

import system.system_operations

s = system.system_operations

os.system('apt-get update -y && apt-get upgrade -y')

os.system('apt-get install bind9 -y')

os.system('dpkg -l bind9')

path_file = '/etc/bind/named.conf.local'

data = s.read_file(path_file)

data = """zone "aula.ads"{
  type master;
  file "/etc/bind/aula.ads.zone";
};

zone "0.16.172.in-addr.arpa"{
  type master;
  file "/etc/bind/named.172.16.0";
};"""

s.write_file(path_file, data)

os.system('named-checkconf')
