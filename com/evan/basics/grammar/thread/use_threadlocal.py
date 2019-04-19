# coding=utf-8
"""
使用ThreadLocal来做线程内部的变量共享有非常大的优势
1. 简化了线程内部变量的传输
2. 可以在不使用锁的情况下，区分出每个线程下面的变量
"""

import threading, time


# 定义全局threadlocal变量
local_school = threading.local()


def process_student():
    """
    获取当前线程关联的student
    :return:
    """
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    """
    绑定threadlocal与student的关系
    :param name:  学生名称
    :return:
    """
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name="Thread-A")
t2 = threading.Thread(target=process_thread, args=('Evan',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
