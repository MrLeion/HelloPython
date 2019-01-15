#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
面向对象高级编程:
__slots__：避免动态给类绑定属性或者方法，仅对当前类起作用

'''
__author__ = 'tzl'


class Student:
    __slots__ = ('name', 'age')  # 限定只能添加 name 和 age 属性

    def __init__(self):
        pass


##########
# Exe1: @property
##########
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



##########
#枚举类
##########
from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


















