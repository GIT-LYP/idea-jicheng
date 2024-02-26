# -*- coding: utf-8 -*- 
# @Time : 2024/2/23 11:20
# @Author : imp
# @File : demo01.py 组织列表

# 使用方法sort()对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#对数组的影响是永久性的，不可逆的
cars.sort(reverse=True)
print(cars)
#sorted 是临时的   reverse函数是翻转   len()是数组的长度

