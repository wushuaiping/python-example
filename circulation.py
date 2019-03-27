#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#---- 学习循环的demos ----#
names = ['Michael', 'Bob', 'Tracy']
print("打印名字")
for name in names:
    print(name)

sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    sum += i
print("计算总和: %s" %sum)

list = range(1, 101)
sum = 0
for i in list:
    sum += i
print("生成0~100的数字，并计算0+1+2..+100的总和: %s" %sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("计算100以内奇数之和：%s" %sum)

names = ['Bart', 'Lisa', 'Adam']
for name in names:
    print("Hello, %s!" %name)

count = 0
while count < 100:
    count = count + 1
    if count > 11:
        break
    print(count)

count = 0
list = []
while count < 100:
    count = count + 1
    if count % 2 == 0:
        continue
    list.append(count)
print("得到一个100以内奇数的集合：%s" %list)