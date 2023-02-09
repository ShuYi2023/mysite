# 传文件之前, 要先 sudo chown /文件夹/


import paramiko
import os
from pathlib import Path

'''
local_path = '/Users/maxmacboookpro2019/my_projs/10django_prjs/mysite/backups/mysite_ng_config'  # *** 本地的绝对路径
remote_path = '/etc/nginx/sites-available/mysite_ng_config'  # *** 远端的绝对路径

local_path = '/Users/maxmacboookpro2019/my_projs/10django_prjs/mysite/backups/mysite.conf'  # *** 本地的绝对路径
remote_path = '/etc/supervisor/conf.d/mysite.conf'  # *** 远端的绝对路径
'''

local_path = '/Users/maxmacboookpro2019/my_projs/10django_prjs/mysite/backups/mysite_ng_config'  # *** 本地的绝对路径
remote_path = '/etc/nginx/sites-available/mysite_ng_config'  # *** 远端的绝对路径

r_dir, r_fullfname = os.path.split(remote_path)
fname, fext = os.path.splitext(r_fullfname)

hostname = '192.168.0.244'
port = 22

username = 'max'
password = '8092'

with paramiko.SSHClient() as client:
    client.load_system_host_keys()
    client.connect(hostname, port, username, password)
    sftp_client = client.open_sftp()

    sftp_client.chdir(r_dir)
    contents_all = sftp_client.listdir()
    contents_with_no_dot = []
    for name in contents_all:
        if name[0] != '.':
            contents_with_no_dot.append(name)

    print(contents_with_no_dot)

    sftp_client.put(local_path, remote_path)  # put or get
    print("file putted")
    # sftp_client.get(remote_path, local_path)  # get remote_path to local_file

# sudo ln -s /etc/nginx/sites-available/mysite_ng_config /etc/nginx/sites-enabled/