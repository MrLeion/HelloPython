#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#########
# 函数式编程
#########

#########
# 高阶函数：函数作为参数传递给函数
#########
def add(x, y, f):
    print(f(x) + f(y))


add(-6, 5, abs)

#########
# 高阶函数：
# Iterator map(函数名，Iterable)
# 1.map 函数的好处在于可以清晰的看出两个数据集合之间的映射关系
# 2.reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 可见 reduce 返回值和定义的映射关系类型一致的
#########



# TODO:exe1:大小写转换
# def normalize(name):
#     for i in range(len(name)):
#         if i == 0:
#             str(name[i]).upper()
#         else:
#             str(name[i]).lower()
#     return name
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# exe2:求和
# from functools import reduce
# def prod(L):
#     if L == None or L == []:
#         return 0
#
#     if len(L) < 2:
#         return L[0]
#     return reduce(lambda x, y: x * y, L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


# TODO:exe3:浮点数转字符串
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def _aboveZero(x, y):
    return 10 * x + y


def _belowZero(x, y):
    return x + y * 0.1



# @param s: a list of char
# @param offset: an integer
# @return: nothing
def rotateString( s, offset):
    # write you code here
    if not offset: return
    if not s: return

    n = len(s)
    offset = offset % n

    for i in range(offset):
        t = s.pop()
        s.insert(0, t)




def char2Num(k):
    return DIGITS[k]


def str2float(s):
    strArray = s.split('.')
    print(strArray)
    if len(strArray) > 1:
        rotateString(strArray[1],2)
        print(strArray[1])
        return reduce(_aboveZero, map(char2Num, strArray[0])) + 0.1 * reduce(_belowZero, map(char2Num, strArray[1]))
    else:
        return reduce(_aboveZero, map(char2Num, strArray[0]))






print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
