#!/usr/bin/env/ python
#Encodign: utf-8

import io
import os
import stat
#52

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

path_file = '/etc/apt/sources.list'
mode = stat.S_IREAD

if os.path.exists(path_file):    
    os.remove(path_file)

touch(path_file)

with open(path_file, 'r') as file:
    data = file.readlines()


data = """deb http://security.debian.org/ jessie/updates main contrib non-free\n
deb http://http.debian.net/debian/ jessie main contrib non-free\n
deb http://http.debian.net/debian/ jessie-updates main contrib non-free\n
deb http://http.debian.net/debian/ jessie-backports main contrib non-free"""

with open(path_file, 'w') as file:
    file.writelines(data)