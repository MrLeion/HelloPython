#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
IO 编程
'''
__author__ = 'tzl'

##########
# 普通文件的同步读取复杂写法
##########


import os


def readFile():
    try:
        path = os.path.abspath(os.path.abspath(os.path.dirname(__file__))) + '/data/data.txt'
        f = open(path, 'r')
        print(f.read())
    except BaseException:
        print('there is something wrong')
    finally:
        if f:
            f.close()


def writeFile(content):
    try:
        dir = os.path.abspath(os.path.abspath(os.path.dirname(__file__))) + '/data'
        if not os.path.exists(dir):
            os.makedirs(dir)
        path = dir + '/data.txt'
        f = open(path, 'w')
        f.write(content)
    except BaseException:
        print('there is something wrong')
    finally:
        if f:
            f.close()


writeFile('tzl')
readFile()




##########
# 普通文件的同步读取简化写法
##########


def readFile():
    path = os.path.abspath(os.path.abspath(os.path.dirname(__file__))) + '/data/data.txt'
    with open(path, 'r') as f:
        print(f.read())


def writeFile(content):
    dir = os.path.abspath(os.path.abspath(os.path.dirname(__file__))) + '/data'
    if not os.path.exists(dir):
        os.makedirs(dir)
    path = dir + '/data.txt'
    with open(path, 'w') as f:
        f.write(content)


writeFile('love')
readFile()




##########
# file-like IO:StringIO&BytesIO
##########
# StringIO
from io import StringIO


f = StringIO()
f.write('x')
f.write(' ')
f.write('s')

print(f.getvalue())


from io import BytesIO
bytes_io = BytesIO()
bytes_io.write('中文'.encode('utf-8'))
print(bytes_io.read())






















