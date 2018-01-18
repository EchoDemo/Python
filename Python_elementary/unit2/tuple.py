#coding:utf-8

#1、tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是tuple一旦创建完毕，就不能修改
#也就是说tuple没有 append()方法，也没有insert()和pop()方法。
#创建tuple和创建list唯一不同之处是用( )替代了[ ]。
t=('Adam', 'Lisa', 'Bart')
print t

#2、因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，导致我们得到
#的不是tuple，而是整数 1。正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个
#逗号“,”，这样就避免了歧义。Python在打印单元素tuple时，也自动添加了一个“,”，为了更明确地告诉你这是一个tuple
L=(1)
print L
L=(1,)
print L

#3、“可变”的tuple：tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，
#指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是
#可变的！
q=('a', 'b', ['A', 'B'])
print q
L=q[2]
L[0] = 'X'
L[1] = 'Y'
print q
