#!usr/bin/env python3
# -*- coding: utf-8 -*-
# python 高级特性：python 可迭代对象
# 验证 是否是可迭代对象：
from collections import Iterable
isinstance([],Iterable)


# 默认是左闭右开的,如果哪边没写代表闭区间，实际左边没写无所谓，重要的是右边
# L = list(range(100))
# print(L)
# print(L[0:10])  # 左闭右开
# print(L[-10:-1])  # 左闭右开
# print(L[-10:])  # 左闭右闭


# Exe1:切片:快速操作list/tuple 和动态数组差不多
def trim(s):
    # 前缀空格索引
    preIndex = 0
    while preIndex < len(s) and s[preIndex: preIndex + 1] == ' ':
        preIndex = preIndex + 1
    print(preIndex)
    s = s[preIndex:]
    # 后缀空格索引
    lastIndex = -1
    while lastIndex >= -len(s) and s[lastIndex - 1:lastIndex] == ' ':
        lastIndex = lastIndex - 1
    print(lastIndex)
    print(len(s))
    print(s[:lastIndex])
    if lastIndex == -1:
        return s[:]
    else:
        return s[:lastIndex]


# 测试:
# if trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')




# Exe2:迭代:python3 可迭代对象
def findMinAndMax(L):
    if L == [] or L is None:
        return (None, None)
    max = min =L[0]
    for i in L:
        if max< i:
            max = i
        if min > i:
            min = i
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



# TypeError: list indices must be integers or slices, not tuple






#Exe3:列表生成式:[执行语句 for 循环 条件]
print([x*x for x in range(1,11) if x%2==0])
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')




# 生成器：(执行语句 for 循环 条件),为可迭代对象 通过for 循环遍历
#使用 yield 定义一个迭代器，当执行语句遇到 yield 的时候回自动返回
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)


#获取 迭代器返回值
g= fib(6)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e.value)
        # 终止循环
        break

# Exe3:杨辉三角
#todo
def triangles():
    pass







#迭代器
# list tuple 等为 Iterable但不是 Iterator,只有 generator 是 Iterator
# next 函数必须让操作对象成为 Iterator，Iterable 可以同过itear() 转化为 Iterator
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance(iter([]),Iterator))
print(isinstance([],Iterable))
print(isinstance(g,Iterator))
print(isinstance(g,Iterable))







