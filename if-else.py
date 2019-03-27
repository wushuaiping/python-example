#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sheAge = 25
myAge = 24
if myAge >= sheAge:
    print('LYJ marry me')
else:
    print('me marry LYJ')

age = input("输入你的年龄:")
if age.isdigit():
    age = int(age)
    if 18 <= age:
        print('你已经%d岁了，可以进入本网站' %age)
    elif 18 > age:
        print('你才%d岁，不可以进入本网站' %age)
else:
    print("你输入的\'%s\'不是数字" %age)
        
x = input("请输入需要进行非空判断的值：")
if x:
    print("你输入的'%s'不是空！" %x)
else:
    print("你输入的'%s'是空！" %x)