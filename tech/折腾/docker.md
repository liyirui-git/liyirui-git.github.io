## Docker

### 0. Win10 Home 版安装docker

Win10 家庭版 2004 版本以后拥有了WSL2 可以使用Docker了。

在我这里无论是Win10 Home 还是 Win10 Pro，Docker都与VMware存在冲突。

结果就是安装完Docker准备运行的时候会遇到：

> Hardware assisted virtualization and data execution protection must be enabled in the BIOS. See https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled

这个问题就是之前安装完VMware解决了它的问题以后给docker的安装造成了问题。

解决方法也很简单，就是在 “Windows 功能” 中，关闭“虚拟机平台”（virtual machine platform），此时电脑会重启。重启以后再开启“虚拟机平台”，又会重启，之后再开启Docker就没有这个问题了。

个人觉得是重装了一下虚拟机的底层支持。因为我之前使用VMware的时候遇到问题，记得通过命令行修改过一些设置。

### 1. 基础命令

#### 1.1 镜像

##### 通过一个镜像新建一个容器：

```
$ docker run -tid -p 8080:8080 --name museum1 museum:0.1 /bin/bash
```

参数说明：

- **-a stdin:** 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；
- **-d:** 后台运行容器，并返回容器ID；
- **-i:** 以交互模式运行容器，通常与 -t 同时使用；
- **-P:** 随机端口映射，容器内部端口**随机**映射到主机的端口
- **-p:** 指定端口映射，格式为：`主机(宿主)端口:容器端口` 
- **-t:** 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
- **--name="nginx-lb":** 为容器指定一个名称；
- **--dns 8.8.8.8:** 指定容器使用的DNS服务器，默认和宿主一致；
- **--dns-search example.com:** 指定容器DNS搜索域名，默认和宿主一致；
- **-h "mars":** 指定容器的hostname；
- **-e username="ritchie":** 设置环境变量；
- **--env-file=[]:** 从指定文件读入环境变量；
- **--cpuset="0-2" or --cpuset="0,1,2":** 绑定容器到指定CPU运行；
- **-m :**设置容器使用内存最大值；
- **--net="bridge":** 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；
- **--link=[]:** 添加链接到另一个容器；
- **--expose=[]:** 开放一个端口或一组端口；
- **--volume , -v:**	 绑定一个卷



##### commit一个新的镜像：

```
$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
```

各个参数说明：

- **-m:** 提交的描述信息
- **-a:** 指定镜像作者
- **e218edb10161：**容器 ID
- **runoob/ubuntu:v2:** 指定要创建的目标镜像名



#### 1.2 容器

##### 停止一个容器的运行

```
$ docker stop [CONTAINER ID]或[CONTAINER NAME]
```



##### 连接一个容器

```
$ docker exec -it [CONTAINER ID] /bin/bash
```

用exec命令的好处是，在从container中使用 `exit` 命令退出时，容器不会停止运行。



##### 本机文件与容器文件相互复制

如果不进容器，在宿主机上操作也可以用docker命令实现宿主机和容器内部的文件交互,以下是在宿主机操作

把宿主机上的文件复制到docker容器内部

    $ docker cp [/path/filename] [CONTAINER ID]:[/path/filename]

也可以把docker容器内部的文件复制到本地

```
$ docker cp [CONTAINER ID]:[/path/filename] [/path/filename]
```



### 2. 扩展功能

### 2.1 用ssh连接docker

假设当前已经得到一个Ubuntu的镜像

##### 1. 将docker的22端口映射到主机的一个端口上

```
$ docker run -tid -p 2022:22 --name xxxx ubuntu:20.04 /bin/bash
```

##### 2. 安装openssh

```
$ apt update
$ apt upgrade
$ apt install vim
$ apt install openssh-server
```

##### 3. 给root设置一个密码

想必到这里docker的虚拟系统中的root账户还没有密码吧

```
$ passwd
```

##### 4. 修改配置文件

```
$ vim /etc/ssh/sshd_config
```

注释这一行**PermitRootLogin prohibit-password**
添加一行**PermitRootLogin yes**

```
# PermitRootLogin prohibit-password
PermitRootLogin yes
```

保存退出

##### 5. 重启ssh

```
$ /etc/init.d/ssh restart
```

##### 6. 在本机进行连接

```
$ ssh root@127.0.0.1 -p 2022
```

看到如下结果即表示连接成功：

```
The authenticity of host '[127.0.0.1]:2022 ([127.0.0.1]:2022)' can't be established.
ECDSA key fingerprint is SHA256:rK0B/Ord927tKmkP23Ql9pGfRq1yJ+CAFpMf+OFokC8.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

