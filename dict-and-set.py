#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#---- dict(等同于Java的map) set的demos ----#
dicts = {'刘雨佳': 99, '吴帅苹': 100, '宁可': 59, '程明远': 0}
print("取得吴帅苹的成绩: %s" %dicts['吴帅苹'])
dicts['刘雨佳'] = 100
print("更改刘雨佳的成绩为：%s" %dicts['刘雨佳'])

#---- 判断dict中的key是否存在，如果不存在直接获取会报错。所以要先判断 ----#
# dicts['AS']
if 'AS' in dicts:
    print("存在")
else:
    print("不存在")

# 通过dict.get('XX')来进行安全的操作
value = dicts.get('AS')
print("value = %s" %value)
if value == None:
    value = dicts.get('宁可')
    print(value)
# set
sets = set([1, 1, 2, 3]) # set不重复会自动过滤重复的数据
print(sets)
# 往set中添加数据
sets.add(4)
print(sets)
# 删除set中的数据
sets.remove(1)
print(sets)
# set的value就是key，所以删除value就是删除的key。
# sets.remove(1)
# print(sets)
# 不可变对象
# list是可变对象，所以可以改变原有list的内容和顺序
s = [2,1,3]
s.sort()
print(s)
# 对str进行replace操作，无法改变原有的值，replace生成的是一个新的值，内存中的指针指向的不是原有的地方，而是新的地方
s = 'abc'
s.replace('a', 'A') # 把'a'替换成'A'
print(s) # 会发现s还是原来的'abc'，并没有改变原来的内容
print(s.replace('a', 'A')) # replace会返回新的值，所以能看到改变的内容。
st = s.replace('a', 'A') # 这时候看st就会看到更改过后的值
print(st)