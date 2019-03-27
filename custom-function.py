#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 自定义一个abs函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("请传入数字类型参数")
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-23), my_abs(2))

# 空函数，使用pass对未想好怎么写的地方进行占位，这样代码运行不会报错
def nop():
    pass

if 2 < 1:
    pass

# 函数返回多个值
import math
# 从x移动到y，移动step步
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

nx, ny = move(100, 100, 60, math.pi / 6)
print(nx, ny)

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("请传入正确的数字")
    if a == 0:
        raise TypeError("a不能为0")

quadratic(1, 1, 2)