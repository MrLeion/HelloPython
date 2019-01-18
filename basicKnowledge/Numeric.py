#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
数值类型
'''
__author__ = 'tzl'

# python 基本数据类型提供了整数，浮点数，字符串
# 注：1.整数精确，浮点数会有误差
# 注：2.r''或者r""表示后面字符串中的转义字符全部失效
# 注：4. %为 % 的转义字符，字符串'%%' 为 %
# 注：int() str() unicode() 坐字符转换
# None 和 '' 类似于 null 和空字符串

# 引号中的引号解决
# 用单引号包裹
# 转移字符




# python 提供了两种 内置集合类型 list 和 tuple
# 注：1.list 用 [] 表示，且可以添加和删除元素
# 2.tuple 用 （） 表示，不可以添加或删除元素，或者说每个元素的内存地址不可改变
# 3.索引正序从 0 开始，逆序从 -1 开始

# python 中内置了对字典 dict 和集合 set 的支持，其中dict 类似于 java 中的Map
# 注：1.增 2.删 pop(key) 对应的键值也消失 3.改 键值不可改变 4.查 1>dict[key] 2>get(key) 3> in







# ex1 :打印 I'm "OK"!
print("I\'m \"OK\" ")
print(r'I'"m '"'OK" ')
# print("I'm ... "OK")
print(r'''hello,\n world''')

# 格式化

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# ex2:计算成绩提升百分点
r = (85 - 72) / 72
print('%.1f %%' % r)

##########
# str:字符串为不可变
##########
a = 'abc'
b = a.replace("a", "A")
print(a, b)

# ex3:list和tuple索引

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])

import math


def quadratic(a, b, c):
    # if not isinstance(a,(int,float)):
    #     raise TypeError("bad type")
    delta = b * b - 4 * a * c
    if delta >= 0:
        return ((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)), ((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a))
    else:
        return -1, -1


print('hahah' + str(1 + 2))

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]


# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
def getStr(headlines):
    count = 0
    result = ''
    for i in range(len(headlines)):
        if count + len(headlines[i]) > 140:
            # 截取字符串到 140
            result = result + headlines[i][:140 - count]
            return result
        result = result + headlines[i] + ' '
        count += len(headlines[i]) + 1
    return result


news_ticker = getStr(headlines)
