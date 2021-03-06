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

path_file = '/etc/bind/aula.ads.zone'

s.touch(path_file)

data = s.read_file(path_file)

data = """
$TTL 604800
@    IN SOA aula.ads. root.aula.ads.(
     200007201       ;serial
     28800           ;refresh
     14400           ;retry
     3600000         ;expire
     84400)          ;minimum
;

www     IN A  172.16.0.1
server  IN A  172.16.0.1

@       IN MX 10  aula.ads.
@       IN NS     aula.ads.
@       IN A      172.16.0.1

"""

s.write_file(path_file, data)

os.system('named-checkconf -z')

os.system('named-checkzone server.aula.ads /etc/bind/aula.ads.zone')

path_file = '/etc/bind/named.172.16.0'

s.touch(path_file)

data = s.read_file(path_file)

data = """
$TTL  604800
@ IN  SOA aula.ads. root.aula.ads. (
      2000072001  ;serial
      28800       ;refresh
      14400       ;retry
      3600000     ;expire
      86400)      ;minimun
;
@ IN  NS  aula.ads.
1 IN  PTR aula.ads

"""

s.write_file(path_file, data)

os.system('named-checkzone -z')

os.system('named-checkzone 1.0.16.172.in.addr-arpa /etc/bind/named.172.16.0')

path_file = '/etc/resolv.conf'

""