# coding=utf-8
"""
该模块主要学习如何使用numpy模块，主要是提供的数据类型和方法
"""

import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

print('b:', b)
print('c: ', c)
print('c.type:', c.dtype)
print('a.shape:', a.shape)
print('c.shape:', c.shape)

# c是一个3行4列的矩阵数组，现将其改成4行三列的矩阵数组
c.shape = 4, 3
print('c', c)

# 当某个轴为-1时，将根据该元素个数自动计算
c.shape = 2, -1
print('c', c)

# shape是直接在原有数组基础上修改，reshape是新创建一个数组，原数组不变，但是指向的是同一块数据区域
d = a.reshape((2, 2))
print('d: ', d)
print('a: ', a)
a[1] = 100
print('d: ', d)

# 创建数组中的数据格式是浮点数和复数的方法
f_array = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype=float)
complex_array = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype=complex)
print('浮点数：', f_array)
print('复数：', complex_array)

# 通过指定开始值、终值和步长来创建一维数组
range_array = np.arange(0, 1, 0.1)
print("arange array:", range_array)

# 通过指定开始值，终值和元素个数来创建一维数组
linspace_array = np.linspace(0, 1, 12)
print('linspace array:', linspace_array)

# 创建等比数列，下面的例子将创建10^0 - 10^2方的20个数字的等比数列
logspace_array = np.logspace(0, 2, 20)
print('logspace array:', logspace_array)

# 使用frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
s = 'abcdefgh'
str_array = np.fromstring(s, dtype=np.int8)
print('fromstring int8:', str_array)
str16_array = np.fromstring(s, dtype=np.int16)
print('fromstring int16:', str16_array)


# 使用fromfuncktion方法创建9*9乘法表
def func(i, j):
    return (i+1) * (j+1)


form_9_9 = np.fromfunction(func, (9, 9))
print(form_9_9)

# 获取一个布尔值类型的数组
x = np.random.rand(10)
print('x:', x)
print('x>0.5:', x > 0.5)
print('[x>0.5]', x[x > 0.5])

"""
生成一个0-55的6*6二位数组的过程：
    1. 首先生成一个(0, 10, 20, 30, 40, 50)的1*6维数组
    2. 将1*6的数组转置成6*1维的数组
    3. 将数组的每一维都与一个1*6的(0,1,2,3,4,5)数组相加
"""
two_array = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6, 1)
print('二维数组生成：\n', two_array)

# 计算0,36,72....360°对应的sin正弦值
sin_value = np.linspace(0, 2*np.pi, 10)
print('sin_value:', sin_value)
y = np.sin(sin_value)
print('sin值：\n', y)






