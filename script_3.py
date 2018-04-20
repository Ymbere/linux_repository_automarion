#!/usr/bin/env/ python
#Encoding: utf-8

import io
import os
import stat

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


os.system('apt-get update && apt-get -y upgrade')
os.system('apt-get -y install samba')

path_file = '/etc/samba/smb.conf'

if os.path.exists(path_file):
    os.remove(path_file)

touch(path_file)

with open(path_file, 'r') as file:
    data = file.readlines()

data = """[global]\n
workgroup = Samba\n
encrypt passwords = yes\n
smb passwd file = /etc/samba/smbpasswd\n
interfaces = eth0\n
bind interfaces only = yes\n
security = user # requerido para controle de acesso dos usuários\n
username level = 2\n
wins support = yes\n
[Producao]\n
comment = Arquivos compartilhados do departamento de Produção\n
browseable = yes\n
path = /home/producao\n
guest ok = yes\n
force create mode = 0666\n
force directory mode = 0777\n
valid users = +producao\n
writable=no\n
write list=jose\n
veto files=/*.mp3/*.mpg/*.mpeg/*.avi/*.jpg/\n
[Vendas]\n
comment = Arquivos compartilhados do departamento de Vendas\n
browseable = yes\n
path = /home/vendas\n
guest ok = yes\n
force create mode = 0666\n
force directory mode = 0777\n
valid users = +vendas\n
writable=no\n
write list=jose\n
veto files=/*.mp3/*.mpg/*.mpeg/*.avi/*.jpg/*.txt\n
[publico]\n
path = /home/publico # caminho do diretório compartilhado na máquina linux\n
public = yes # “yes” indica que todos podem visualizar este diretório\n
public = yes # “yes” indica que todos podem visualizar este diretório\n
only guest = yes\n
writable = yes # permite que todos os usuários possam gravar neste diretório\n"""

with open(path_file, 'w') as file:
    file.writelines(data)

os.system('groupadd Samba')
os.system('groupadd producao')
os.system('groupadd vendas')
os.system('adduser --no-create-home jose')
os.system('adduser jose producao')
os.system('smbpasswd -a jose')
os.system('adduser --no-create-home antonio')
os.system('adduser antonio producao')
os.system('smbpasswd -a antonio')
os.system('adduser --no-create-home paula')
os.system('adduser paula vendas')
os.system('smbpasswd -a paula')
os.system('adduser --no-create-home carolina')
os.system('adduser carolina vendas')
os.system('smbpasswd -a carolina')
path1 = '/home/producao'
if os.path.exists(path1):
    os.remove(path1)
os.system('mkdir /home/producao')
path2 = '/home/vendas'
if os.path.exists(path2):
    os.remove(path2)
os.system('mkdir /home/vendas')
path3 = 'mkdir /home/publico'
if os.path.exists(path3):
    os.remove(path3)
os.system('mkdir /home/publico')
os.system('mksmbpasswd /etc/passwd > /etc/samba/smbpasswd')
