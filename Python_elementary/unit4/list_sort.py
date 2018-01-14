#coding:utf-8

#1、使用sort()对列表进行永久性排序；
cars=['bmw','audi','toyota','subaru']
cars.sort() #按字母顺序排列(永久性的)
print(cars)
cars.sort(reverse=True) #按字母逆序排列(永久性的)
print(cars)

#2、使用函数sorted()对列表进行临时排序；
cars=['bmw','audi','toyota','subaru']
print(cars)
print(sorted(cars)) #临时排序；
print(sorted(cars,reverse=True)) 
print(cars)

#3、永久性倒着打印列表；
cars.reverse()
print(cars)

#4、确定列表的长度；
print(len(cars))
