# coding=utf-8
"""
函数返回结果是一个函数的操作
"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
# 打印f时，此时内部函数加和功能还没有开始计算，只是做了一个标记，f表示的是一个函数
print(f)
# 如果是打印f()，则表明要计算函数的结果，所以返回的是最终加和结果
print(f())


# 为何f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
# 原因是在打印时方法执行中i已经全部等于3了
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# 让count方法返回正常的结果
def count():
    fs = []
    def f(n):
        def j():
            return n*n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())