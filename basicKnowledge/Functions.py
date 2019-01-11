# 调用函数 python 内置函数：https://docs.python.org/3/library/functions.html
##python3.x 中的函数可以取别名,这个别名对象指向函数对象
##python 中提供了很多内置函数包括 类型转换，时间等类似于java.utils 包的功能
a = hex
print(a(255))
print(a(1000))




# 定义函数
# 定义函数 def 函数名(参数)：
# 空函数需要加 pass
# 当需要函数返回多个值，函数返回 tuple
# 导入函数 from 文件名 import 函数名
# 定义函数无需指定返回参数类型，python 会自行解析并且只返回一个

#定义函数
def my_abs(x):
    if x>0:
        return x
    else:
        return -x



#空函数
def nop():
    pass




#应用函数
from Numeric import quadratic
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')







#python 中函数参数具有比较多的新特性：
# 1.默认参数必须在必须参数之后，默认参数一般考虑到函数接口的兼容性问题

def power(n):
    return n*n

def power(x,n =2):
    m =1
    while n>0:
        m = x*m
        n = n-1
    return m

print(power(5))
































# demo:递归函数

#
# def fact(n):
#     if n ==1:
#         return n
#     return n*fact(n-1)



# 尾递归：递归形式在递归是只调用函数本身，
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1,product*num)


def fact(n):
    return fact_iter(n,1)



# OOM
# print(fact_iter(1000,1))
# print(fact(1000))




# Exe：汉诺塔问题
def move(n,_from,_buffer,_to):
    if n==1:
        print(_from,'-->',_to)
    else:
        # 把 n-1 号盘子移动到缓冲区
        # 把1号从起点移到终点
        # 然后把缓冲区的n-1号盘子也移到终点
        move(n-1,_from,_to,_buffer)
        print(_from, '-->', _to)
        move(n-1,_buffer,_from,_to)

move(3, 'A', 'B', 'C')










