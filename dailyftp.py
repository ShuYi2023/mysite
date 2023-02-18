# -*- coding:utf:8 -*-

import pysftp
import os
import codecs
import re
import time

files_dic = {1: "/mnt/ubshare/projects/static",
             2: "/home/my/u3d/u3d/settings.py",
             3: "/home/my/u3d",
             4: "u3d_nginx.conf",
             5: "u3d_uwsgi.ini",
             6: "uwsgi_params",
             7: "db.sqlite3"
             }
sitepath = "/home/my/u3d"  # 最前面有一个斜杠
bakpath = "/home/my/u3d/ybak"
yfilename = '/home/my/Desktop/projects/zz/ypas.html'
cnopts = pysftp.CnOpts()
# cnopts.hostkeys = None
yusername = 'my'
cloud = '111.231.57.45'
yremote = cloud


def bakup_uwsgi_nginx():
    # 备份nignx文件
    os.chdir(bakpath)
    yftp.get('/etc/uwsgi/sites/u3d_uwsgi.ini', )
    yftp.get('/etc/systemd/system/uwsgi.service')
    yftp.get('/etc/nginx/sites-available/u3d_nginx')
    yftp.get('/home/my/u3d/u3d/settings.py', '/home/my/u3d/ybak/settingsBak')
    yftp.get('/mnt/ubshare/projects/static/css/blog.css','/home/my/u3d/ybak/blogbak.css')
    yftp.get('/mnt/ubshare/projects/static/css/script.js','/home/my/u3d/ybak/scriptbak.js')
    print("uwsgi, nginx 配置文件备份完成.")

def upload_dir(ydir='/home/my/u3d'):
    ''' 用于上传目录，ydir='/home/my/u3d' '''
    with yftp.cd(ydir):
        print("begin..")
        sourcepath = remotepath = ydir
        yftp.put_r(sourcepath, remotepath)
        print("done with uploading dir..")


with codecs.open(yfilename, 'r', encoding='utf-8') as fypas:
    lines = fypas.readlines()
if lines:
    line = lines[99].strip()
    line_frags = line.split()
    # print(line_frags)
    ypss1 = str(int(line_frags[1]) - int(line_frags[0]))
    cloud_pss = line_frags[2] + ypss1 + line_frags[-1]
    print(cloud_pss)
ypass = cloud_pss

'''
sourcepath=files_dic[2]
remotepath=files_dic[2]
print(sourcepath)
'''

with pysftp.Connection(yremote, username=yusername, password=cloud_pss) as yftp:
    # !!!别偷懒，运行之前先关闭服务器上的uwsgi服务

    print(time.strftime('%H:%M:%S', time.localtime(time.time())))
    #print("stopping uwsgi..")
    # yftp.execute("sudo systemctl stop uwsgi.service")
    #print("uwsgi stopped and updating begins..")

    # *************
    yftp.get('/mnt/ubshare/projects/static/css/blog.css','/home/my/u3d/ybak/blogbak.css')
    yftp.get('/mnt/ubshare/projects/static/css/script.js','/home/my/u3d/ybak/scriptbak.js')

    # *************
    #print('下面执行命令：sudo systemctl start uwsgi')
    #yftp.execute("sudo systemctl start uwsgi")
    # yftp.execute("sudo systemctl reboot")
    #print('命令执行完毕，uwsgi已启动。')
    print(time.strftime('%H:%M:%S', time.localtime(time.time())))

    '''
    bakup_uwsgi_nginx_settings()
    upload_dir('/mnt/ubshare/projects/static/css')  # 上传css和js文件，如blog.css
    upload_dir()  # 默认参数是 /home/my/u3d
    yftp.put('/home/my/u3d/ybak/settingsBak', '/home/my/u3d/u3d/settings.py')
    yftp.put('/home/my/u3d/ybak/settingsBak','/home/my/u3d/u3d/settings.py')
    yftp.put('/home/my/u3d/account/views.py','/home/my/u3d/account/views.py')
    yftp.put('/home/my/u3d/blog/templates/blog/base.html','/home/my/u3d/blog/templates/blog/base.html')
    图片之前已经由surfacePro上传了，
    print('命令：nohup uwsgi --ini u3d_uwsgi.ini &')
    # 在Linux下对图片进行压缩的命令如下：
    # os.system('find . -name "*.png" | xargs optipng')
    #upload_dir('/home/my/u3d/blog/templates') #上传templates
    upload_dir('/mnt/ubshare/projects/static') #重装系统要用，用于上传所有图片
    remotefile = os.path.join(sitepath, files_dic[i])
    upload_dir('/mnt/ubshare/projects/static/u3d01')
    upload_nginx() # 恢复ngix设置文件, !!!注意，这里没有恢复原来的db.sqlite3
    下面代码不管用，要手动启动 
    1）切换到u3d目录，启动uwsgi。
    2）命令：nohup uwsgi --ini u3d_uwsgi.ini & #这个&符号很重要哦

    print("start uwsgi..")
    with yftp.cd("u3d"):
        yftp.execute("nohup uwsgi --ini u3d_uwsgi.ini &")
    print("uwsgi started.")
    '''
