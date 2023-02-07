#!/usr/bin/python

import paramiko
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
full_filename = 'settings.py'  # *** 输入文件名. 分清楚 dir, path, name 和 extension
local_path = os.path.join(BASE_DIR,'mysite', full_filename)  # 版本 1
# local_path = os.path.join(BASE_DIR, full_filename)  # *** 看看是否用 版本 1

remote_path = '/home/max/mysite/mysite/' + full_filename  # *** 远端的绝对路径
r_dir, r_fullfname = os.path.split(remote_path)
fname, fext = os.path.splitext(full_filename)

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
