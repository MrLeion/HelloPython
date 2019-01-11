#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
文档注释
'''
_author_ = "tzl"




#上述总结：
#第一行 shabang 指定脚本的解释器，意即从 Path环境变量中寻找 Python3
#第二行 文件的编码格式
#第3-5行 模块的文档注释
#第6行 模块的作者名称




#定义模块
# 文件名即模块名
# Python 中包一般内部会有 _init_.py



# 使用模块
import math


#当内部运行时 __name__ 为 main ,即主入口；
#从外部导入当前模块则条件不成立，main 入口函数不会运行，和 Java 是同理的
if __name__ == '__main__':
   print(math.sqrt(2))



#这里注意到__name__ 这种特殊的命名方式是 Python 中所特有的：
# 常见的字母数字命名默认是 public 属性的
# 前缀有下划线后缀没有的默认是 private 属性，这里官方不建议由外部引用，但是外部引用了后也是可以通过编译的
# 前后缀都是两条下划线的，为特殊变量如__author__,__name__等



#python 内置了一些常用模块，但是一些第三方模块需要通过 pip3 进行安装
#另外，如果知道模块的名称可以去pypi 网站进行查询






