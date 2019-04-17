# coding=utf-8
"""
dict:类似于java中的map容器，使用键值对进行存储，dict的key必须是不可变对象
    一、其中当使用方式dict[key]根据key获取某个值，key不存在时会报错，一般采用有两种方式：
        1. 判断字典中是否存在key， key in dict
        2. 当key不存在时，返回一个默认值，dict.get(key) or dict.get(key, default)
    二、dict和list对比，有以下特点：
        1. 查找和插入的速度极快，不会随着key数量的增加而变慢
        2. 需要占用大量的内存

Set：是一组key的集合，但是不存储value，key不能重复
     set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
"""
# 字典相关操作
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

# Set相关操作
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)