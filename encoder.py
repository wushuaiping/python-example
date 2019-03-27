#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# x = '哈哈'
# print(x.decode('utf-8'))
# print('%s, hello! 你的调休还有%d天。你的年假还有%d天' % ('吴帅苹', 10, 7))
# print('亲爱的%s, 您好。您的余额为%f' %('吴帅苹', 10000000.012))

s1 = 72
s2 = 85
r = (85 - 72) / 72.0 * 100
print((85 - 72))
str = '小明的成绩提升了{0:.1f}%'.format(r)
str1 = '%s的成绩提升了%.1f%%' %('小明', r)
print(str)
print(str1)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
