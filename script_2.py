# !/usr/bin/env/ python
# Encoding: utf-8

from system.system_operations import SystemOperations

s = SystemOperations

path_file = '/etc/apt/sources.list'

s.remove_path_if_exists(path_file)

s.touch(path_file)

with open(path_file, 'r') as file:
    data = file.readlines()


data = """deb http://security.debian.org/ jessie/updates main contrib non-free\n
deb http://http.debian.net/debian/ jessie main contrib non-free\n
deb http://http.debian.net/debian/ jessie-updates main contrib non-free\n
deb http://http.debian.net/debian/ jessie-backports main contrib non-free"""

s.write_file(path_file, data)
