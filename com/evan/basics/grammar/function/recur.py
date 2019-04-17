# coding=utf-8
"""
利用递归函数计算阶乘
"""


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))


# 利用递归函数移动汉诺塔
def move(n, a, b, c):
    if n == 1:
        print("move", a, '-->', c)
    else:
        # 首先考虑是将剩余的n-1个盘子都已经移动到了辅助盘b
        move(n-1, a, c, b)
        # 然后将a上的最后一个盘子移动到c
        move(1, a, b, c)
        # 此时b上有n-1个盘，a变成了辅助盘，将b上的盘子移动到c
        move(n-1, b, a, c)


move(4, 'A', 'B', "C")

