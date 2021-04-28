## 在Ubuntu上安装MySQL

需要注意的一点是，Ubuntu18之后，都是默认MySQL8.0版本，所以如果需要MySQL5.7版本的话，最高选择Ubuntu18.04，不然的话会有点麻烦。如果想要查看 MySQL 8.0 版本的安装教程，可以参考-->[链接](https://blog.csdn.net/weixx3/article/details/94133847)

我这里用到的环境是：

Ubuntu 18.04 和 MySQL 5.7

### 安装MySQL

只需要输入下述命令：

```
$ apt update
$ apt install mysql-server
```

### 配置MySQL

```
$ mysql_secure_installation
```

需要配置的项目如下，其中的选项作为参考：

```
#1
VALIDATE PASSWORD PLUGIN can be used to test passwords...
Press y|Y for Yes, any other key for No: N (我的选项)

#2
Please set the password for root here...
New password: (输入密码)
Re-enter new password: (重复输入)

#3
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them...
Remove anonymous users? (Press y|Y for Yes, any other key for No) : N (我的选项)

#4
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network...
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : Y (我的选项)

#5
By default, MySQL comes with a database named 'test' that
anyone can access...
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : N (我的选项)

#6
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Y (我的选项)
————————————————
版权声明：本文为CSDN博主「Weison Wei」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixx3/article/details/80782479
```

配置完成以后可以开启服务

```
$ /etc/init.d/mysql start
```

### 配置远程访问

通过下面的命令进入到mysql中

```
$ mysql -uroot -p
```

在其中输入

```
mysql> GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY "123456";
```

其中`root@localhos`，`localhost`就是本地访问，配置成`%`就是所有主机都可连接；

第二个`'123456'`为你给新增权限用户设置的密码，`%`代表所有主机，也可以是具体的ip；
不过这设置了`%`但我root通过工具还是登陆不进去，可能是为了安全性，所以新建数据库和用户；



### 新建数据库和用户

用root用户新建数据和用作远程访问的用户

```
##1 创建数据库weixx
mysql> CREATE DATABASE weixx;
##2 创建用户wxx(密码654321) 并允许wxx用户可以从任意机器上登入mysql的weixx数据库
mysql> GRANT ALL PRIVILEGES ON weixx.* TO wxx@"%" IDENTIFIED BY "654321"; 
```

然后就可以啦



### 备注

上面的命令绝大多数都需要root权限，这里因为是在docker容器中配置，所以没有加sudo。



### 参考链接

https://blog.csdn.net/weixx3/article/details/80782479



## Linux下MySQL的使用

### 数据库的sql文件导入导出

〇、登录

```
$ mysql -u root -p
```

一、导出数据库用mysqldump命令（注意mysql的安装路径，即此命令的路径）：

1、导出数据（命令行命令）：

```
$ mysqldump -u用户名 -p密码 数据库名 > 数据库名.sql
```

二、导入数据库（sql命令）：

1、首先建空数据库

```
mysql> create database abc;
```


2、导入数据库

（1）选择数据库

```
mysql> use abc;
```


（2）设置数据库编码

```
mysql> set names utf8;
```


（3）导入数据（注意sql文件的路径）

```
mysql> source /home/abc/abc.sql;
```

注意：有命令行模式，有sql命令

### 显式命令

1、显示数据库列表。 

```
mysql> show databases; 
```

 2、显示库中的数据表： 

```
mysql> use mysql;
mysql> show tables; 
```

 3、显示数据表的结构：

```
mysql> describe 表名; 
```

 4、建库： 

```
mysql> create database 库名; 
```

 5、建表： 

```
mysql> use 库名； 
mysql> create table 表名 (字段设定列表)； 
```

 6、删库和删表: 

```
mysql> drop database 库名; 
mysql> drop table 表名； 
```

 7、将表中记录清空： 

```
mysql> delete from 表名;
```

 8、显示表中的记录： 

```
mysql> select * from 表名;
```

