#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
numpy 学习

1.numpy 设计初衷被用来进行科学计算的，底层运用 C 语言编写的，因此在**矩阵运算**方面凸显出非常优越的性能
2. pandas 是基于numpy 开发出来的，所以具有着 比numpy 更加优越的性能

'''
__author__ = 'tzl'


import numpy as np

##########
#每一个对象都有自己的属性
#矩阵有维度，行列数，总元素个数
##########

# 初始化一个单位矩阵
unitMatrix = np.array([[1, 0,0], [0, 1,0]])

# 每一个对象都有自己的属性
#矩阵有维度，行列数，总元素个数

print(unitMatrix)
print('矩阵的维数：',unitMatrix.ndim)
print('行：'+str(unitMatrix.shape[0])+'列：'+str(unitMatrix.shape[1]))
print('元素的个数：'+str(unitMatrix.size))


##########
#作为矩阵运算的特别支持模块，如果不对一些特殊矩阵有啥便捷操作，都不好意思叫 numpy 啦~~
#下面来看下矩阵：
#注意：矩阵和列表相似，都是存放相同类型，因此我们也可以指定数组的类型
##########
# 生成特定数型的矩阵

print('生成特定数型的矩阵')
unit_matrix_float = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.float)
print(unit_matrix_float)
print(unit_matrix_float)
print(unit_matrix_float.dtype)
unit_matrix_int32 = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.int32)
print(unit_matrix_int32)
print(unit_matrix_int32.dtype)
unit_matrix_int64 = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.int64)
print(unit_matrix_int64)
print(unit_matrix_int64.dtype)


# 生成零矩阵
print("零矩阵:")
print(np.zeros((3,4)))

# 生成全空矩阵
print("全空矩阵:")
print(np.empty((3,4)))


# 连续数组，类似 python 中的range() 函数
print('连续数组')
print(np.arange(10,20,2))



# 生成线性等分
print("线性等分:")
print(np.linspace(0,1,4))



# 改变矩阵维度
print("改变矩阵维度:")
print(np.arange(0,12).reshape(3,4))





##########
# 矩阵运算
##########






