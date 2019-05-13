# coding=utf-8
"""
该模块主要研究numpy中提供的方法
"""

import numpy as np
import time, math

def test_sin():
    """
    比较math和numpy中sin的运算速度
    :return:
    """
    start = time.clock()
    x = [math.sin(i*0.001) for i in range(1000000)]
    print('math.sin:', time.clock() - start)

    x = [i*0.001 for i in range(1000000)]
    x = np.array(x)
    start = time.clock()
    np.sin(x, x)
    print('numpy.sin:', time.clock() - start)


if __name__ == "__main__":
    test_sin()


