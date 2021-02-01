## autossh内网穿透

参考：https://www.jianshu.com/p/7accc1e485d3

有时候调用接口需要在内网开发机上来调试，但回调的时候可能无法直接回调到开发机上，因此可以开启autossh，找一台有外网IP的机器，配置成代理机器，代理回调到内网开发机上，流程如下：

##### 1 配置sshd

```ruby
$ vim /etc/ssh/sshd_config
```

##### 2 设置GatewayPorts

```undefined
GatewayPorts yes
```

##### 3 重启sshd

```ruby
$ sudo service sshd restart
```

##### 4 在被代理的机器上，安装autossh

```ruby
$ sudo apt install autossh
```

##### 5 开启穿透服务

```ruby
$ autossh -M 5678 -CNR 8081:0.0.0.0:8080 root@116.62.62.62
```

5678为随便使用一个端口，用来与代理服务器交互，8081为代理服务器上的端口，8080为被代理服务器上的端口，116.62.62.62为代理服务器IP地址。
 浏览器访问  http://116.62.62.62:8081 即可代理到内网 127.0.0.1:8080 端口上

##### 6 具体实践

代理服务器使用的是我在西雅图的Hostwind服务器，需要按照上面的要求，去sshd_config开启 GatewayPorts。

第一次虽然打开了GatewangPorts，但是依旧不通，所以将具体的sshd_config给出：

```
#   $OpenBSD: sshd_config,v 1.101 2017/03/14 07:19:07 djm Exp $

# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_dsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key

# Ciphers and keying
#RekeyLimit default none

# Logging
#SyslogFacility AUTH
#LogLevel INFO

# Authentication:

#LoginGraceTime 2m
#PermitRootLogin prohibit-password
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

#PubkeyAuthentication yes

# The default is to check both .ssh/authorized_keys and .ssh/authorized_keys2
# but this is overridden so installations will only check .ssh/authorized_keys
AuthorizedKeysFile  .ssh/authorized_keys

#AuthorizedPrincipalsFile none

#AuthorizedKeysCommand none
#AuthorizedKeysCommandUser nobody

# For this to work you will also need host keys in /etc/ssh/ssh_known_hosts
#HostbasedAuthentication no
# Change to yes if you don't trust ~/.ssh/known_hosts for
# HostbasedAuthentication
#IgnoreUserKnownHosts no
# Don't read the user's ~/.rhosts and ~/.shosts files
#IgnoreRhosts yes

# To disable tunneled clear text passwords, change to no here!
#PasswordAuthentication yes
#PermitEmptyPasswords no

# Change to no to disable s/key passwords
#ChallengeResponseAuthentication yes

# Kerberos options
#KerberosAuthentication no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes
#KerberosGetAFSToken no

# GSSAPI options
#GSSAPIAuthentication no
#GSSAPICleanupCredentials yes

# Set this to 'yes' to enable PAM authentication, account processing,
# and session processing. If this is enabled, PAM authentication will
# be allowed through the ChallengeResponseAuthentication and
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication via ChallengeResponseAuthentication may bypass
# the setting of "PermitRootLogin without-password".
# If you just want the PAM account and session checks to run without
# PAM authentication, then enable this but set PasswordAuthentication
# and ChallengeResponseAuthentication to 'no'.
UsePAM yes

#AllowAgentForwarding yes
#AllowTcpForwarding yes
#GatewayPorts no
#X11Forwarding no
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes
#PrintMotd yes
#PrintLastLog yes
#TCPKeepAlive yes
#UseLogin no
#PermitUserEnvironment no
#Compression delayed
#ClientAliveInterval 0
#ClientAliveCountMax 3
#UseDNS no
#PidFile /var/run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
#ChrootDirectory none
#VersionAddendum none

# pass locale information
AcceptEnv LANG LC_*

# no default banner path
#Banner none

# override default of no subsystems
Subsystem   sftp    /usr/libexec/sftp-server

# Example of overriding settings on a per-user basis
#Match User anoncvs
#   X11Forwarding no
#   AllowTcpForwarding no
#   PermitTTY no
#   ForceCommand cvs server

# XAuthLocation added by XQuartz (http://xquartz.macosforge.org)
XAuthLocation /opt/X11/bin/xauth```

GatewayPorts yes
```

在实验室的Gaia上，用的涛哥的bash脚本 ProxySH

```bash
#!/bin/bash

REMOTE_IP=104.168.234.196
REMOTE_USER=root

yirui_proxy(){
    autossh -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R ${REMOTE_IP}:${1}:${2}:${3} ${REMOTE_USER}@${REMOTE_IP}
}

yirui_proxy 8100 buaadml.info 22
yirui_proxy 8101 anna.buaadml.info 22
yirui_proxy 8102 betty.buaadml.info 22
yirui_proxy 8104 danny.buaadml.info 22 
yirui_proxy 8105 ella.buaadml.info 22
yirui_proxy 8106 faery.buaadml.info 22 
yirui_proxy 8109 i.buaadml.info 22


exit 0
```

