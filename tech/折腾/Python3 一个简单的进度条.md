### 使用 Python3 制作一个简单的进度条



```python
import sys
import math
import time


def progress_bar(portion, total):
    """
    total 总数据大小，portion 已经传送的数据大小
    :param portion: 已经接收的数据量
    :param total: 总数据量
    :return: 接收数据完成，返回True
    """
    length = 50             # 进度条的长度
    part = total / length  
    count = math.ceil(portion / part)
    sys.stdout.write('\r')
    sys.stdout.write(('[%-50s] %d/%d %.2f%%' % (('>' * count), portion, total, portion / total * 100)))
    sys.stdout.flush()

    if portion >= total:
        sys.stdout.write('\n')
        return True

# 调用方式
portion = 0
total = 1000
while True:
    time.sleep(0.2)
    portion += 10
    sum = progress_bar(portion, total)
    if sum:
        break
print("Finish")

```



输出结果：

```
[>>>>>>>>>>>>>>>>>>>                               ] 380/1000 38.00%
```

