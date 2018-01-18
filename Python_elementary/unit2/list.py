#coding:utf-8

#1、list
classmates=['Michael',100,'Tracy']
print classmates #打印classmates变量的内容

#2、顺序访问list，注意不要越界。
L=['Adam', 'Lisa', 'Bart']
print L[0]
print L[1]
print L[2]

#3、倒序访问list，注意也不要越界。
print L[-1] #表示倒数第一个元素
print L[-2] #表示倒数第二个元素
print L[-3] #表示倒数第三个元素

#4、list的append()方法添加新元素。append()总是把新的元素添加到list的尾部。list的 insert()方法，添加到指定的
#位置，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素。
L.append('Jack')
print L
L.insert(1,'Paul')
print L

#5、list的pop()方法默认删除最后一个元素。 pop(2)把指定位置的元素删除。
L.pop()
print L
L.pop(1)
print L
del L[1] #删除指定位置的元素。
L.remove('Adam') #根据元素值删除元素。且只删除第一个指定的值。

#6、对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变。
L[0] = 'Paul'
print L

#7、使用range()创建数字列表：
numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2)) #打印1~10内的偶数
print(even_numbers)

squares=[]
for x in range(1,11):
	square=x**2
	squares.append(square)
print(squares)

#8、统计数字列表；
print(min(squares))
print(max(squares))
print(sum(squares))

