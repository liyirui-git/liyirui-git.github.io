## Win10 Home 版安装docker

Win10 家庭版 2004 版本以后拥有了WSL2 可以使用Docker了。

在我这里无论是Win10 Home 还是 Win10 Pro，Docker都与VMware存在冲突。

结果就是安装完Docker准备运行的时候会遇到：

> Hardware assisted virtualization and data execution protection must be enabled in the BIOS. See https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled

这个问题就是之前安装完VMware解决了它的问题以后给docker的安装造成了问题。

解决方法也很简单，就是在 “Windows 功能” 中，关闭“虚拟机平台”（virtual machine platform），此时电脑会重启。重启以后再开启“虚拟机平台”，又会重启，之后再开启Docker就没有这个问题了。

个人觉得是重装了一下虚拟机的底层支持。因为我之前使用VMware的时候遇到问题，记得通过命令行修改过一些设置。
