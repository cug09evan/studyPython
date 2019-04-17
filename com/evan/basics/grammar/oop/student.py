# coding=utf-8
"""
学习Python面向对象编程
类是一个抽象的概念，对象是一个具象的概念
"""
__author__ = 'evan zhang'
__date__ = '2019-4-14'


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name=', bart.name)
print('lisa.name=', lisa.name)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

bart.age = 17
print('bart\'age=', bart.age)