#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def bmiCalculate(height, weight):
    bmi = weight / (height ** 2)
    return bmi

height = input("请输入您的身高(m)\n")
weight = input("请输入您的体重(kg)\n")
height = float(height)
weight = float(weight)
bmi = bmiCalculate(height, weight)
print("您的身高是：%sm" %height)
print("您的体重是：%skg" %weight)
print("您的BMI指数是：%s" %bmi)
str = "评判结果为："
if bmi < 18.5:
    print(str + "过轻")
elif bmi >= 18.5 and bmi <= 25:
    print(str + "正常")
elif bmi > 25 and bmi <= 28:
    print(str + "过重")
elif bmi > 28 and bmi <= 32:
    print(str + "肥胖")
elif bmi > 32:
    print(str + "严重肥胖")