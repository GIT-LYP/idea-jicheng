# name  = ['imp', 'zhangsan', 'lisa']
# #修改元素。
# name[0] = 'wangerxiao'
# # 增加元素
# name.append('ltw')
#
# name.insert(1,'tom')
#
# # 删除元素
# # 直接删除不能继续使用它的值
# # del name[1]
# # 能继续使用它的值pop,也就是说存储了pop的值，pop的值还能表现出来，但是这个值在数组中已经被删除，pop中可以删除任意位置（）中添加数字。
# poped_name = name.pop(0)
# print(name)
# print(poped_name)
#
# for i in name:
#
#     print( "this is my friend:"+i)




#根据值删除元素

# store = ['煎饼','火腿','蛋挞']
#
# store.remove("煎饼")
# print(store)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

