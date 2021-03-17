# Python不加载图片获取尺寸

### 解释

网上其他人的说法基本都不太可行，恭喜你找到了宝藏。
通常在 Python 里读取尺寸时都会把整张图片加载到内存中，非常耗时，有没有办法像 Andorid 加载 Bitmap 时一样快速读取尺寸而不加载图片呢？答案是有的，使用 imagesize。

### 下载

    pip install imagesize

### 使用

```python
import imagesize


def main():
	input_path = ''
	width, height = imagesize.get(input_path)

if __name__ == '__main__':
	main()
```

