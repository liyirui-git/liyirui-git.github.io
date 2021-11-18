## Python执行windows的cmd命令行

注意，Windows下的cmd和powershell存在一定的区别，这里以cmd场景介绍。

目前了解到的主要有两种方法：

#### 1. os.system(command)

例如：

```python
>>> import os
>>> ret = os.system("ls")
test.py
>>> print(ret)
0
```

这种方式输入的就是字符串形式的命令，但是在Linux和Windows上面略有不同，在Linux上，返回值为执行命令的exit值；而在Windows上，返回值是运行后，shell的返回值。

**注意，该方法无法得到运行命令的输出。**



#### 2. os.popen()

例如：

```python
import os

adb = "adb devices"
d = os.popen(adb)
f = d.read()
print(f)
```

这种方式的输入也是以字符串的形式，但是返回值是可以得到运行命令的输出。



### CMD中如何一行执行多条命令

参考：https://www.cnblogs.com/gtea/p/12673156.html

CMD在一行中执行多条命令可以使用如下三种分隔符分开：`&`、`&&`和`||`。

用&隔开，用法是前后命令不管是可否运行都会运行下去，1命令&2命令，就是运行1命令，运行2命令。

用&&隔开，用法是前面的命令运行成功才运行后面的命令，1命令&2命令，就是运行1命令没出错、运行成功才运行2命令。

用||隔开，用法是前面的命令运行成功才运行后面的命令，1命令&2命令，就是运行1命令出错、运行不成功才运行2命令。
拷贝