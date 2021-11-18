## Python如何SSH远程连接

### 如何使用

这里需要用到库 paramiko

> conda install paramiko

为了可以方便连接服务器发送命令，我封装了一个小的函数：

```python
def ssh_cmd(cmd, hostname, username):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout_message = stdout.read().decode('utf-8')
    if stderr:
        print("[Error Message]")
        print(stderr.read().decode('utf-8'))
    ssh.close()
    return stdout_message
```



这里需要注意的是，要执行的命令需要放在cmd一个字符串里一次性发过去，也就是说不支持“多轮对话”。所以多条指令要使用符号";"分开。

例如：

```sh
cd /home/; ls;
```



同时，也看到网上有一些比较好的改进。

- 因为当前的Paramiko只能在执行完命令以后才返回终端的输出信息，有人对其进行了改进，实现了实时输出：https://cloud.tencent.com/developer/article/1352425
- 也有人对paramiko进一步做了封装：https://blog.csdn.net/m0_38039437/article/details/101606656



### 激活conda环境

paramiko登录后，只获得路径（/usr/local/bin:/bin:/usr/bin）

因为密码存在于被连接机器的/etc/ssh/sshd_config配置文件里吗

sshd服务默认把（/usr/local/bin:/bin:/usr/bin）作为PATH的值

故在调用conda 及python时，需要加载环境变量

所以我发给服务器的命令里多加了一个conda命令：

```python
conda_cmd = "export PATH=\"/home/xxxx/miniconda3/bin:$PATH\";source activate; conda activate ispreid2;"
```

然后再执行 `python xxxx.py`。

参考链接：https://blog.csdn.net/miao_007/article/details/110916497