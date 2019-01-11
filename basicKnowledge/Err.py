#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一：try-except-finally 在任何高级语言中都是实用的，并且细节方面都是一致的
# 二：BaseException 是所有错误的基类，继承关系：https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# 三：出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
# 四：通过 logging 收集错误日志是最常用的方法


# 记录错误的常用方式
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except ZeroDivisionError as e:
        logging.exception(e)

main()