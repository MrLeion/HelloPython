#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
运算符
'''
__author__ = 'tzl'

# 一：python 中 缩进代表程序体 和 Java 中的大括号相同
# 二：在 if 判断中注意：
#     1.加上 ：
#     2.关键字 if elif else
#       if <条件判断1>:
#           <执行1>
#       elif <条件判断2>:
#           <执行2>
#       elif <条件判断3>:
#           <执行3>
#       else:
#           <执行4>
# 三：逻辑运算符：
#       1.is 两个对象地址一致，== 值相同



sum = 0
for x in range(101):
    sum = sum + x
print(sum)


# demo:条件判断 异常处理
birth = input('birth: ')
try:
    if int(birth) < 2000:
        print('00前')
    else:
        print('00后')
except BaseException as e:
    print("error:", e)
finally:
    print('haha finally')

import logging

# Ex1:条件判断：BMI
weight = input("weight:")
height = input("height:")

try:
    bmi = float(weight) / (float(height) * float(height))
    if bmi < 18.5:
        print('过轻'+str(bmi))
    elif bmi < 25:
        print('正常'+str(bmi))
    elif bmi < 28:
        print('过重'+str(bmi))
    elif bmi < 32:
        print('肥胖'+str(bmi))
    else:
        print('严重肥胖'+bmi)

except BaseException as e:
    logging.exception(e)
finally:
    print('hahah')



