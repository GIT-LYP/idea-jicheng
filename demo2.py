# -*- coding: utf-8 -*- 
# @Time : 2024/2/23 13:50
# @Author : imp
# @File : demo2.py 遍历整个列表

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!\n")
#
# print("Thank you, everyone. That was a great magic show!")

# 创建数值列表
# for value in range(1,8):
#     print(value)
#
# num = list(range(1,5,2))
# print(num)
# 乘方的小运算

squares = []
for i in range(1,10):
    square = i **2
    squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析

name = [value**2 for value in range(1,10)]
print(name)
