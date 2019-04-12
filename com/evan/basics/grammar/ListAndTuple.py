# coding=utf-8
"""
  该类主要用于对Python的list和tuple等类数组的基本语法进行探索：
    list：数据可变，提供丰富的操作函数，并且list中的元素类型也可以是多种多样的
    tuple：数据一旦初始化，则不可变，很像java中的Enum操作，但是tuple中所谓的不变，指的是每个元素指向永远不变，
            但是若元素中存在一个list，则list中的数据是可变的，但是指向list元素这个元素不可变
"""
"""定义list数据"""
classmates = ["evan", "nick", "clair"]

"""下面将对list列表中常用的方法进行简单的介绍"""
# 判断list列表长度
len(classmates)
# 获取索引对应的数据
classmates[0]
classmates[-1]
# 追加数据到list末尾
classmates.append("jack")
# 追加数据到list指定索引位置
classmates.insert(1, "lucy")
# 删除list末尾的元素
classmates.pop()
# 删除指定位置元素
classmates.pop(2)
# 给某个索引下的数据重新赋值
classmates[1] = "monkey"

'''定义tuple元祖'''
# 若元组中只有一个元素，则一定要加, 否则定义的变量将会被认为不是元组
tuple1 = (1,)
tuple2 = (1, 2, ["money", "freedom"])
tuple2[2][0] = "mind"

