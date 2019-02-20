#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
adb 命令
'''
__author__ = 'tzl'

##########
# python 运用两种方式调用adb：
# os.system()
# os.popen()
# 两者的区别是前者无返回值，后者有返回值
#
# subprocess 执行内部命令
##########
import os
import sys

print(os.system('adb version'))

print(os.system('adb devices'))

#
process = os.popen('adb shell getprop ro.product.device')
output = process.read()
print(output)

#
process = os.popen('adb shell getprop ro.build.version.release')
output = process.read()
print(output)

process = os.popen('adb shell wm density')
output = process.read()
print(output)

process = os.popen('adb shell wm size')
output = process.read()
print(output)

# 540 965 10 300 200

print(sys.path[0])

##########
# exit(1):means there was some issue / error / problem and that is why the program is exiting.
# exit(0):means a clean exit without any errors / problems
# exit(-1) = exit(255)
##########
print(sys.version_info.major)
