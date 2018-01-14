#coding:utf-8

#1、定义元组：其值无法修改。
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0]=250 #此处无法修改。

#2、遍历元组：
for x in dimensions:
	print(x)

#3、修改元组变量(虽然无法修改元组，但可以重新定义元组)
dimensions=(400,100)
for x in dimensions:
	print(x)

