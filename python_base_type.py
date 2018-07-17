#Author Scong
# -*- coding utf-8 -*-
#help()


#三个连续的单引号或者双引号，可以保存输入格式
'''
sentence="""hello
world
and
welcome"""
print(sentence)'''


#字符串的切片
'''
str="python"
print(str[2:4])     #字符串的截取，起始下标包含，结束下标不包含
print(str[::2])     #步长为2进行截取,默认是1
print(str[1::2])    #步长为2进行截取
print(str[::-1])    #步长为负，表示自右向左截取'''


#列表
'''
list1 = [1,2,3,4,5,6,'a','leexiaomei','c',[10,20,30]]
print(len(list1))   #打印列表的长度
print(list1[-1][-1])    #截取list1列表中的最后一个，然后在截取出来的结果上，截取最后一个
print(list1[7][3:])
list1.append("Scong")   #向列表追加元素
print(list1)
del list1[0]        #删除下标0的元素
print(list1)
list2=[1,344,5,6,7,433,0]
print(max(list2))'''

#字典,是key-value（键值对形式存在的，没有顺序，通过键取出值）
mydir = {'name':'lee','age':21}
print("长度为：\t",len(mydir))
print("名字：\t", mydir['name'] + "\n年龄：\t",mydir['age'])

# blist = alist
# clist = alist[:]
# id(clist)