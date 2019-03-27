#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list = ['Spring', 'DingDang']
print(list)
print(list[0])
print(list[1])
print('last element: %s' %list[len(list) - 1])
print('use -1 get last element: %s' %list[-1])
print('use -2 get penult element: %s' %list[-2])
list.append('Dave')
print('use append(): %s' %list)
list.insert(2, 'Iva')
print('use insert(2, \'Iva\'): %s' %list)
list.insert(-2, 'Simple')
print('use insert(-2, \'Simple\'): %s' %list)
list.pop()
print('use list.pop(): %s' %list)
list.pop(0)
print('use list.pop(0): %s' %list)
s = ['PHP', 'JAVA', list]
print(s)
print('get %s' %s[2][1])
print('s len:%s' %len(s))
tuple1 = ('Spring', 'DingDang')
print('安全的tuple: ' , tuple1)
tuple2 = (2,)
print('消除数学意义的歧义:', tuple2)
tuple3 = (1, 2, 3, 4, tuple2, list)
print('tuple + list: ', tuple3)
list = ['Change']
tuple3 = (1, 2, 3, 4, tuple2, list)
print('改变tuple中的list的值: ', tuple3)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print('打印Apple: ', L[0][0])
print('打印Python: ', L[1][1])
print('打印Lisa: ', L[2][2])