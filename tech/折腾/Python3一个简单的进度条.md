### 使用 Python3 制作一个简单的进度条



```python
import sys
import time


def progress_bar(portion, total, length=50):
    """
    total 总数据大小，portion 已经传送的数据大小
    :param portion: 已经接收的数据量
    :param total: 总数据量
    :param length: 进度条的长度
    :return: 接收数据完成，返回True
    """
    sys.stdout.write('\r')
    temp_str = '[%-' + str(length) + 's] %d/%d %.2f%%'
    count = int(portion * length / total)
    sys.stdout.write((temp_str % (('>' * count), portion, total, portion / total * 100)))
    sys.stdout.flush()

    if portion >= total:
        sys.stdout.write('\n')
        return True

# 调用方式
portion = 0
total = 100
while True:
    time.sleep(0.2)
    portion += 1
    sum = progress_bar(portion, total)
    if sum:
        break
print("Finish")

```



输出结果：

```
[>>>>>>>>>>>>>>>>>>>                               ] 380/1000 38.00%
```

