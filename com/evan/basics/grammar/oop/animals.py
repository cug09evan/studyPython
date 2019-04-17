# coding=utf-8
"""
该类主要为了学习Python的多态
"""


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running')


class Cat(Animal):
    def run(self):
        print('cat is running')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()


print('a is animal? ', isinstance(a, Animal))
print('a is Dog? ', isinstance(a, Dog))
print('a is Cat? ', isinstance(a, Cat))

print('d is animal? ', isinstance(d, Animal))
print('d is Dog? ', isinstance(d, Dog))
print('d is Cat? ', isinstance(d, Cat))

run_twice(c)