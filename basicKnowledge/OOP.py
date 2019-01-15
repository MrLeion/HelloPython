#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
面向对象编程:
构造器：def __init__(self,***）,双下划线开头和结尾，第一个参数为 self
封装：私有成员 双下划线开头,一般程度 一个下划线开头。实际上都是可以访问的，一个下划线可以通过 对象调用，两个下划线可以通过 对象._类名成员变量 的形式访问
继承：class 类名(父类)
多态：鸭子类型(有相同方法即可)
获取对象信息的重要方法：
type() isInstance()
 dir() 对象所有属性和方法
 getattr(obj,属性名) 获取对象属性
 setattr(obj,属性名，值) 设置对象属性
 hasattr(obj,属性名) 判断是否存在
'''
__author__ = 'tzl'


# demo: 类 构造器 封装
class Student():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 数据封装
    def print_age(self):
        print('%s:%s' % (self.__name, self.__age))


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            return
        self.__gender = gender

    def get_gender(self):
        return self.__gender



##########
#继承
##########
class Master(Student):
    pass





if __name__ == '__main__':
    bart = Student('Bart', 'male')
    print(dir(bart))
    print(getattr(bart, '_Student__name'))
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')
