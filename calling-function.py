#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 绝对值
print(abs(-2))
# 拿最大的值
arr = [1, 2, 3, 4, 5]
print(max(arr))
# 数据类型转换
a = int('1')
print(a)
b = float('1.23')
print(b)
c = str(123)
print(c)
d = bool(1)
print(d)
e = bool(2)
print(e)
f = bool('')
print(f)
# 变量指向函数
g = int
h = g('1')
print(h)
# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
n1 = hex(n1)
n2 = hex(n2)
print(n1, n2)