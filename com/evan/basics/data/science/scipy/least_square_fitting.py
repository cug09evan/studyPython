# coding=utf-8
"""
scipy库中提供最小二乘拟合算法
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as pl


def func(x, p):
    """
    数据拟合所用的函数：A*sin(2*pi*k*x + theta)
    :param x:
    :param p:
    :return:
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x + theta)


def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，
    :param p: 拟合需要找到的系数
    :param y:
    :param x:
    :return:
    """
    return y - func(x, p)


x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6  # 真实数据的函数参数
y0 = func(x, [A, k, theta])  # 真实数据
y1 = y0 + 2 * np.random.randn(len(x))  # 加入噪声之后的实验数据

p0 = [7, 0.2, 0]  # 第一次猜的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(y1, x))

print('真实参数：', [A, k, theta])
print('拟合参数：', plsq[0])

pl.plot(x, y0, label=u"real")
pl.plot(x, y1, label=u"noise")
pl.plot(x, func(x, plsq[0]), label=u"nihe")
pl.legend()
pl.show()
