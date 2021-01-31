##### 第一步 先在本地生成公钥

```
ssh-keygen -t RSA -b 800   
```

![img](Ubuntu ssh-keygen 生成公钥并添加到远程服务器上.assets/911925-20180509143857772-591744705.jpg)

也可以直接输入：`ssh-keygen` 然后一路回车

##### 第二步 进入到.ssh文件夹下

```
cd /root/.ssh
```

##### 第三步 将本地的公钥发送到远程服务器

```
ssh-copy-id -i id_rsa.pub [远程服务器IP]
```

![img](Ubuntu ssh-keygen 生成公钥并添加到远程服务器上.assets/911925-20180509144215938-1221928971.jpg)

这一步需要输入远程服务器的root密码

##### 第四步 测试登录远程服务器

![img](Ubuntu ssh-keygen 生成公钥并添加到远程服务器上.assets/911925-20180509144421615-1546265366.png)

 

搞定 ！！ 