# coding=utf-8
"""
主要学习如何使用Python的多进程,由于fork函数只有在Unix类系统下才有用，所以为了兼容所有平台，需要使用Process

创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
"""

from multiprocessing import Process
import os
import time


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    time.sleep(10)


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end...')