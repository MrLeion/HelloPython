#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
什么？编码问题
没有的事~~
'''
__author__ = 'tzl'

import sys, locale

print("代码默认编码格式：", sys.getdefaultencoding())
print("系统源码默认保存格式：", sys.getfilesystemencoding())
print("系统源码默认保存格式：", locale.getdefaultlocale())

##########
# Python3 中需要关注的是str(字符)和bytes(字节)之间的关系
##########
a = 'a'
print(a, type(a))

print('中国'.encode('utf-8'))
print(len('中国'.encode('utf-8')))

# ascii 不支持中文编码
# print('中国'.encode('ascii'))



print('ABC'.encode('utf-8'))
print(len('ABC'.encode('utf-8')))

# 忽略错误字节 errors='ignore'
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

b = b'a'
print(b, type(b))
