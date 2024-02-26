# -*- coding: utf-8 -*- 
# @Time : 2024/2/23 15:30
# @Author : imp
# @File : car.py
# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())#全字母大写
#     else:
#         print(car.title())#首字母大写

# 练习8-1：消息　编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print('我学习了函数')

display_message()
# 练习8-2：喜欢的图书　编写一个名为favorite_book()的函数，其中包含一个名为title的形参。这个函数打印一条消息，下面是一个例子。
def favorite_book(title):
    print(f'One of my favorite books is {title}.')

favorite_book('Alice in Wonderland')

# One of my favorite books is Alice in Wonderland.
#
# 调用这个函数，并将一本图书的名称作为实参传递给它。


