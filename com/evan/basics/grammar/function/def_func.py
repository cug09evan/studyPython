# coding=utf-8
"""
主要学习如何定义函数
"""
import math


'''定义计算绝对值的函数'''


def my_abs(x):
    if not isinstance(int, float):
        raise TypeError('bad oper and type')
    if x > 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad oper and type
my_abs('123')
