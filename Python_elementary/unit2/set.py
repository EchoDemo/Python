#coding:utf-8

#1、set持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。创建set
#的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：s = set(['A', 'B', 'C'])。可以查看 set 的内容：
#print s。请注意，上述打印的形式类似 list， 但它不是 list，仔细看还可以发现，打印的顺序和原始 list 的顺序有可能
#是不同的，因为set内部存储的元素是无序的。因为set不能包含重复的元素，所以，当我们传入包含重复元素的 list时，
#set会自动去掉重复的元素。
s = set(['A', 'B', 'C','C'])
print s
a=len(s)
print a


#2、set存储的是无序集合，所以我们没法通过索引来访问。访问 set中的某个元素实际上就是判断一个元素是否在set中。
#我们可以用 in 操作符判断：'Bart' in s 结果是：True
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
print 'Bart' in s
print 'bart' in s


#3、set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。set存储的元素和
#dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。set存储的元素也是没有顺序的。
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x='MON'
if x in weekdays:
    print 'input ok'
else:
    print 'input error'


#4、由于set也是一个集合，所以,遍历set和遍历list类似，都可以通过 for 循环实现。 for 循环在遍历set时，元素的顺
#序和list的顺序很可能是不同的，而且不同的机器上运行的结果也可能不同。
s = set(['Adam', 'Lisa', 'Bart'])
for name in s:
    print name


#5、由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：一是把新的元素添加到set中，二是把已有元素
#从set中删除。添加元素时，用set的add()方法：s.add(4)。如果添加的元素已经存在于set中，add()不会报错，但是不会
#加进去了。删除set中的元素时，用set的remove()方法：s.remove(4)。如果删除的元素不存在set中，remove()会报错。
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
	if x in s:
		s.remove(x)
	else:
		s.add(x)
print s
