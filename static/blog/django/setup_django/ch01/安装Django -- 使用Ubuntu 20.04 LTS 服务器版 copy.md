# 安装Django -- 使用Ubuntu 20.04 LTS 服务器版

## Ubuntu服务器版的下载地址

* 在Windows中制作安装盘

    - √下载地址: http://releases.ubuntu.com/focal/, 这是: Ubuntu 20.04.5 LTS (Focal Fossa)
    
    - √在 Windows 电脑中用 rufus 把 iso 文件写入到一个 U盘, 8G 的U盘是可以的。
    
## 安装Ubuntu注意事项

- 如果是在旧电脑上安装, 使用的是无线 wifi, 最好在安装过程中就配置好网络.
    - (不推荐的做法: 手动配置网络时, 用 Python 脚本把修改好的 /etc/netplan/00----wifi.yaml 文件 put 到服务器相应目录.)
- (也可以装到 virtual box 中)
    
    - 这种情况下, 不用要Uattended模式. 偏要用的话, 会没有admin的权限.
        
    - 个人用于实验的话, √4核4G就可以了, √硬盘用25G也可以了.
    ![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230929122725.png)
    - 配置摘要如下:
        ![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230929122819.png)
* 按照下图配置好网络.
![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230929122931.png)

## 从MacBook终端用ssh访问服务器

### 服务器连接 Wifi

- √编辑配置文件. 仔细阅读命令后面的注释。
    
```Bash
ip a  # 查看网络的名称
sudo su # 获得 root 权限
cd /etc/netplan/ # 进入相关目录
ls  # 查看目录下的文件
nano 00-installer-config-wifi.yaml
```

- √编辑配置文件内容。以下内容仅供参考, 请根据自己环境中的网络配置。
    
```bash
# This is the network config written by 'max'
network:
  wifis:
    wlp4s0:
      dhcp4: no  # 不自动分配网址
      dhcp6: no
      addresses: [192.168.1.244/24]  # 设置静态网址
      gateway4: 192.168.1.1  # 网关
      nameservers:  # 域名服务器
        addresses: [114.114.114.114, 233.5.5.5, 9.9.9.9, 8.8.8.8]
      access-points:
        "max_tp_mesh":
          password: "xxxxxxxx"
  version: 2  # 必须是 version 2
```

- 启动服务.
    
```Bash
sudo netplan generate
sudo netplan apply
```

### 获得服务器的 ip 地址

- 在服务器中运行命令: `ip a`
    

### √用下图的ssh方式访问

![image.png|450](https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230929131900.png)

## 安装Python3.10

- √Ubuntu 20.04 默认的 Python 是 3.8 版本的, 因此要√在 Ubuntu 20.04 系统中安装 python3.10
    
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.10  # 会安装最新版的 3.10.9.
    
    # 安装 venv
    sudo apt install python3.10-venv -y  # 3.10 不能省略
    
    # 如果要删除
    sudo add-apt-repository --remove ppa:deadsnakes/ppa
    sudo apt remove --autoremove python3.10
    ```
    
## 创建虚拟环境

```bash
max@ubserver:~$ mkdir envs
max@ubserver:~$ cd envs
max@ubserver:~/envs$ python3.10 -m venv dj4 # 创建虚拟环境, 3.10 不能省略

max@ubserver:~/envs$ ls dj4/
bin  include  lib  lib64  pyvenv.cfg  share

max@ubserver:~/envs$ source /home/max/yenvs/dj4/bin/activate  # 激活虚拟环境

(dj4) max@ubserver:~/envs$ 
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ django # 安装 Django

(dj4) max@ubserver:~$ python -m  django --version # 查看 Django 版本
4.1.6

(dj4) max@ubserver:~$ ls / # 查看根目录
cd ~ # 到用户的 home, 相当于 /home/max

```

## 激活虚拟环境

```
source /home/max/yenvs/dj4/bin/activate
```

## 安装 Django, 使用科大的源 -- 清华和豆瓣的慢

```
pip install django -i https://pypi.mirrors.ustc.edu.cn/simple/
```

## [部署和更新Django项目](部署和更新Django项目.md)



## 从局域网的另一台电脑访问 Django服务器: 192.168.1.244:**8000

- √在Django项目的 setting.py 中设置好 
```
ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1', '192.168.0.244']
```

- √把修改好的配置文件上传到服务器
    
- √启动服务器, 注意绿色的部分--**要给定** **ip** **和****端口** :
    
    - `(dj4)` **`max@u22`**`:`**`~/mysite`**`$ python manage.py` `runserver 0.0.0.0:8000`
        
    - 访问的时候, 要访问 `0.0.0.0:8000`, 不要写成√`0.0.0.0``/``8000`--折腾了 15 分钟
        
    - 有了 gunicorn 后, 直接访问192.168.1.244即可, 后面不用写`:8000` .

    ## 服务器操作常用命令

### 修改文件名:

- `sudo mv former_name new_name`
    
### chown 修改文件的 owner

- `chown owner_name file_name`
    
    - `sudo chown max 00-installer-config-wifi.yaml`
        
- `chown owner_name file_dir/` # 文件夹要带斜杠
    
### 获得root权限

- `sudo su # 用于移动文件`
    

### 移动文件

- `sudo path new-path`
    

### 查看电量:

- `upower --dump | grep --color=never -E "state|to\ full|to\ empty|percentage"`
    
### 合盖不休眠的设置

- `sudo nano /etc/systemd/logind.conf`
    
```bash
# See logind.conf(5) for details.

[Login]
#HandleHibernateKey=hibernate
#HandleLidSwitch=suspend
HandleLidSwitch=ignore
#HandleLidSwitchExternalPower=suspend
```

### `reboot` 重新启动

- `然后要等一分钟才会真正 reboot`
    

### `logout` 退出登录状态:

### 设置时区

`sudo timedatectl set-timezone Asia/Shanghai`

`date` # 查看时间

### 用 sftp 的方式上传文件夹到服务器

- 开 sftp 窗口: 在终端输入命令: sftp max@192.168.0.xxx
    
- 上传文件夹: 一定要有 -r (recursive)参数, 目标文件夹是 /home/max/, 不是/home/max~~/mysite~~
    

```Bash
# 上传文件夹: 
put -r /Users/maxmacboookpro2019/my_projs/10django_prjs/mysite/ /home/max/
```

