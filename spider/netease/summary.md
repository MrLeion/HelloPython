- 网页爬虫需要查看网页的编码格式






# 实战笔记

> 问题1️：UnicodeDecodeError ：'gb2312' codec can't decode bytes：illegal multibyte sequence

解决方案：GB2312 < GBK < GB18030

分析：本例中所爬链接：http://news.163.com/rank/ 的 charset 为 GB2312。所以解码格式肯定是 GB2312。但是很尴尬的报了这个错，结果大家也能看到，由于在中文字符编码集的兼容性方面
GB2312 < GBK < GB18030，经过对三种字符集的尝试我们发现 GB18030 很好的满足了我们的需求；


发问：这里我们都知道网页是字节流形式（bytes类型）的。我们这里如果使用 Gbk 可以，那么使用 uincode utf-8 这种编码集不是更好嘛
但是答案很尴尬，由此引发了第二个问题。

>问题二： UnicodeDecodeError: 'utf-8' codec can't decode byte.

解决方案：line.decode("utf8","ignore")






